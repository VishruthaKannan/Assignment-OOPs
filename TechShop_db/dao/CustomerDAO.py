class CustomerDAO:
    def __init__(self, db_connector):
        self.conn = db_connector.open_connection()

    def create_customer(self, customer):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
            VALUES (?, ?, ?, ?, ?)
        """, (customer.first_name, customer.last_name, customer.email, customer.phone, customer.address))
        self.conn.commit()
        return cursor.lastrowid

    def update_customer(self, customer_id, email=None, phone=None, address=None):
        cursor = self.conn.cursor()
        if email:
            cursor.execute("UPDATE Customers SET Email=? WHERE CustomerID=?", (email, customer_id))
        if phone:
            cursor.execute("UPDATE Customers SET Phone=? WHERE CustomerID=?", (phone, customer_id))
        if address:
            cursor.execute("UPDATE Customers SET Address=? WHERE CustomerID=?", (address, customer_id))
        self.conn.commit()

    def get_customer(self, customer_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Customers WHERE CustomerID=?", (customer_id,))
        return cursor.fetchone()
