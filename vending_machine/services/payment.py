from exceptions.invalid_denomination_exception import InvalidDenominationException

class Payment:
    def __init__(self):
        self.accepted_coins = [0.25, 0.50, 1.00]
        self.accepted_notes = [5, 10, 20]

    def validate_coin(self, coin):
        if coin.value not in self.accepted_coins:
            raise InvalidDenominationException("Invalid coin denomination.")

    def validate_note (self, note):
        if note.value not in self.accepted_notes:
            raise InvalidDenominationException("Invalid note denomination.")
