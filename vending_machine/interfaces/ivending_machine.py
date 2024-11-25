from abc import ABC, abstractmethod

class IVendingMachine(ABC):
    @abstractmethod
    def insert_coin(self, coin):
        pass

    @abstractmethod
    def insert_note (self, note):
        pass

    @abstractmethod
    def select_product(self, product_name):
        pass
