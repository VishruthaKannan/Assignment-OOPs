class OrderDAO:
    def __init__(self, db_connector):
        self.conn = db_connector.open_connection()

    def create_order(self, order):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Orders (CustomerID, OrderDate, TotalAmount, Status)
            VALUES (?, ?, ?, ?)
        """, (order.customer_id, order.order_date, order.total_amount, "Processing"))
        self.conn.commit()
        return cursor.lastrowid

    def update_order_status(self, order_id, status):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Orders SET Status=? WHERE OrderID=?", (status, order_id))
        self.conn.commit()

    def get_order_status(self, order_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT Status FROM Orders WHERE OrderID=?", (order_id,))
        return cursor.fetchone()
