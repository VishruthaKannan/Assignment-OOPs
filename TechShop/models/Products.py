from exceptions.CustomExceptions import InvalidDataException

class Products:
    def __init__(self, product_id, product_name, description, price):
        if price < 0:
            raise InvalidDataException("Price must be non-negative.")
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price

    def GetProductDetails(self):
        print(f"ProductID: {self.product_id}, Name: {self.product_name}, Price: {self.price}")