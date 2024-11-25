from abc import ABC, abstractmethod

class IPayment(ABC):
    @abstractmethod
    def validate_coin(self, coin):
        pass

    @abstractmethod
    def validate_note (self, note):
        pass
