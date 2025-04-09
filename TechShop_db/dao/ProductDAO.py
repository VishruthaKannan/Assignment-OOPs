class ProductDAO:
    def __init__(self, db_connector):
        self.conn = db_connector.open_connection()

    def add_product(self, product):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Products (ProductName, Description, Price)
            VALUES (?, ?, ?)
        """, (product.product_name, product.description, product.price))
        self.conn.commit()
        return cursor.lastrowid

    def update_product(self, product_id, price=None, description=None):
        cursor = self.conn.cursor()
        if price is not None:
            cursor.execute("UPDATE Products SET Price=? WHERE ProductID=?", (price, product_id))
        if description:
            cursor.execute("UPDATE Products SET Description=? WHERE ProductID=?", (description, product_id))
        self.conn.commit()

    def get_product(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Products WHERE ProductID=?", (product_id,))
        return cursor.fetchone()
