from models.Customers import Customers
from models.Products import Products
from models.Orders import Orders
from models.OrderDetails import OrderDetails
from models.Inventory import Inventory
from exceptions.CustomExceptions import (
    InvalidDataException,
    InsufficientStockException,
    IncompleteOrderException,
    PaymentFailedException
)

from collections import defaultdict
import datetime

# Sample product inventory (product_id as key)
product_list = []
inventory = {}

# Sample customer
customer1 = Customers(1, "Alice", "Smith", "alice@example.com", "1234567890", "123 Tech Street")

# Create products
try:
    product1 = Products(101, "Smartphone", "Android phone", 299.99)
    product2 = Products(102, "Laptop", "Gaming laptop", 899.99)
    product_list.extend([product1, product2])

    # Add inventory
    inventory[101] = Inventory(1, product1, 50, datetime.datetime.now())
    inventory[102] = Inventory(2, product2, 30, datetime.datetime.now())

except InvalidDataException as e:
    print(e)

# Place an order
try:
    # Check stock
    if not inventory[101].IsProductAvailable(2):
        raise InsufficientStockException("Not enough smartphones in stock.")
    if not inventory[102].IsProductAvailable(1):
        raise InsufficientStockException("Not enough laptops in stock.")

    # Create order
    order = Orders(1001, customer1, datetime.datetime.now(), 0.0)

    # Create order details
    detail1 = OrderDetails(1, order, product1, 2)
    detail2 = OrderDetails(2, order, product2, 1)

    # Update inventory
    inventory[101].RemoveFromInventory(2)
    inventory[102].RemoveFromInventory(1)

    # Calculate order total
    order.total_amount = detail1.CalculateSubtotal() + detail2.CalculateSubtotal()

    print(f"Order placed! Order ID: {order.order_id}")
    print(f"Customer: {order.customer.get_full_name()}")
    print(f"Total Amount: ${order.total_amount}")
    print(f"Order Status: {order.status}")

    # Display inventory value
    print(f"Total Inventory Value: ${inventory[101].GetInventoryValue() + inventory[102].GetInventoryValue()}")

except (InvalidDataException, InsufficientStockException, IncompleteOrderException, PaymentFailedException) as e:
    print(f"Error: {e}")

# Search product
def search_product_by_name(products, name):
    matches = [p for p in products if name.lower() in p.product_name.lower()]
    return matches

print("\n--- Search Results for 'smart' ---")
for product in search_product_by_name(product_list, "smart"):
    product.GetProductDetails()

# Low stock warning
print("\n--- Low Stock Products ---")
for inv in inventory.values():
    if inv.quantity_in_stock < 10:
        print(f"Low stock: {inv.product.product_name} (Qty: {inv.quantity_in_stock})")

# List all products
print("\n--- All Products in Inventory ---")
for inv in inventory.values():
    print(f"{inv.product.product_name} - Qty: {inv.quantity_in_stock}")