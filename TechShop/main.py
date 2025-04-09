from db.DatabaseConnector import DatabaseConnector
from dao.CustomerDAO import CustomerDAO
from dao.ProductDAO import ProductDAO
from dao.OrderDAO import OrderDAO
from entity.Customers import Customers
from entity.Products import Products
from entity.Orders import Orders
from entity.OrderDetails import OrderDetails
from entity.Inventory import Inventory
from exception.CustomExceptions import InvalidDataException, InsufficientStockException, IncompleteOrderException
import datetime

def main():
    print("=== Welcome to TechShop ===")
    db_connector = DatabaseConnector()
    conn = db_connector.open_connection()

    customer_dao = CustomerDAO(db_connector)
    product_dao = ProductDAO(db_connector)
    order_dao = OrderDAO(db_connector)

    # --- Fetch and Display Customers ---
    print("\n[Customers in DB]")
    customers = customer_dao.get_all_customers()
    for cust in customers:
        print(f"{cust.customer_id} - {cust.first_name} {cust.last_name}")

    # --- Fetch and Display Products ---
    print("\n[Available Products]")
    products = product_dao.get_all_products()
    for prod in products:
        print(f"{prod.product_id}: {prod.product_name} - ${prod.price}")

    # --- Register New Customer (Example) ---
    try:
        print("\n[Registering New Customer]")
        new_customer = Customers(0, "Alice", "Wonder", "alice@wonder.com", "1234567890", "Fantasy Lane")
        customer_id = customer_dao.create_customer(new_customer)
        print(f"New Customer Registered with ID: {customer_id}")
    except InvalidDataException as e:
        print("Error:", e)

    # --- Create New Product (Example) ---
    try:
        print("\n[Adding New Product]")
        new_product = Products(0, "Wireless Earbuds", "Bluetooth 5.2, Noise Cancelling", 59.99)
        product_id = product_dao.create_product(new_product)
        print(f"New Product Added with ID: {product_id}")
    except InvalidDataException as e:
        print("Error:", e)

    # --- Place an Order (Example) ---
    try:
        print("\n[Placing Order]")
        customer = customers[0]
        product = products[0]
        quantity = 2

        if product_dao.get_product_stock(product.product_id) < quantity:
            raise InsufficientStockException("Not enough stock to place order.")

        order = Orders(0, customer.customer_id, datetime.datetime.now(), 0)
        order_id = order_dao.create_order(order)

        order_detail = OrderDetails(0, order_id, product.product_id, quantity)
        subtotal = order_detail.calculate_subtotal(product.price)
        order.total_amount = subtotal
        order_dao.update_order_total(order_id, subtotal)

        product_dao.decrease_stock(product.product_id, quantity)

        print(f"Order placed with ID: {order_id} for ${subtotal}")

    except (InvalidDataException, InsufficientStockException, IncompleteOrderException) as e:
        print("Order Error:", e)

    print("\n[Order Status Check]")
    status = order_dao.get_order_status(order_id)
    print(f"Order {order_id} Status: {status[0] if status else 'Not found'}")

    db_connector.close_connection()
    print("\n=== TechShop Session Completed ===")

if __name__ == "__main__":
    main()
