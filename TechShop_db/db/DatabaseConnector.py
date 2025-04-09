import sqlite3

class DatabaseConnector:
    def __init__(self, db_name="techshop.db"):
        self.db_name = db_name
        self.conn = None

    def open_connection(self):
        if not self.conn:
            self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def close_connection(self):
        if self.conn:
            self.conn.close()
            self.conn = None
