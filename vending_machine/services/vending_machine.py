from models.transaction import Transaction
from services.inventory import Inventory
from services.payment import Payment
from exceptions.insufficient_funds_exception import InsufficientFundsException
from exceptions.out_of_stock_exception import OutOfStockException

class VendingMachine:
    def __init__(self, products):
        self.inventory = Inventory(products)
        self.payment = Payment()
        self.transaction = Transaction()

    def insert_coin(self, coin):
        self.payment.validate_coin(coin)
        self.transaction.add_amount(coin.value)

    def insert_note (self, note):
        self.payment.validate_note (note)
        self.transaction.add_amount(note.value)

    def select_product(self, product_name):
        try:
            product = self.inventory.get_product(product_name)
            if self.transaction.amount_inserted >= product.price:
                self.inventory.dispense_product(product_name)
                change = self.transaction.amount_inserted - product.price
                self.transaction.reset()
                return change
            else:
                self.transaction.reset()
                raise InsufficientFundsException("Insufficient funds.")
        except OutOfStockException:
            change = self.transaction.amount_inserted
            self.transaction.reset()
            return change
