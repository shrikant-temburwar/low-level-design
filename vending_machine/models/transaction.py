class Transaction:
    def __init__(self):
        self.amount_inserted = 0

    def add_amount(self, amount):
        self.amount_inserted += amount

    def reset(self):
        self.amount_inserted = 0
