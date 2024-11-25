from exceptions.out_of_stock_exception import OutOfStockException

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def reduce_quantity(self):
        if self.quantity > 0:
            self.quantity -= 1
        else:
            raise OutOfStockException(f"{self.name} is out of stock.")
