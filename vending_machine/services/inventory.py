from exceptions.out_of_stock_exception import OutOfStockException

class Inventory:
    def __init__(self, products):
        self.products = {product.name: product for product in products}

    def get_product(self, product_name):
        if product_name in self.products:
            return self.products[product_name]
        else:
            raise OutOfStockException(f"{product_name} is out of stock.")

    def dispense_product(self, product_name):
        product = self.get_product(product_name)
        product.reduce_quantity()
