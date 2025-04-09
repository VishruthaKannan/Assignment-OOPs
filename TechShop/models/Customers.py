class Customers:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__address = address

    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    def GetCustomerDetails(self):
        print(f"CustomerID: {self.__customer_id}, Name: {self.get_full_name()}, Email: {self.__email}")

    def UpdateCustomerInfo(self, email=None, phone=None, address=None):
        if email: self.__email = email
        if phone: self.__phone = phone
        if address: self.__address = address