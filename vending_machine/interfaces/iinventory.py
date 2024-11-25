from abc import ABC, abstractmethod

class IInventory(ABC):
    @abstractmethod
    def get_product(self, product_name):
        pass

    @abstractmethod
    def dispense_product(self, product_name):
        pass
