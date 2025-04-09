class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock, last_stock_update):
        self.inventory_id = inventory_id
        self.product = product
        self.quantity_in_stock = quantity_in_stock
        self.last_stock_update = last_stock_update

    def IsProductAvailable(self, quantity_to_check):
        return self.quantity_in_stock >= quantity_to_check

    def RemoveFromInventory(self, quantity):
        if self.quantity_in_stock >= quantity:
            self.quantity_in_stock -= quantity

    def GetInventoryValue(self):
        return self.product.price * self.quantity_in_stock