from datetime import datetime

class Drug:
    def __init__(self, name, quantity, expiry_date):
        self.name = name
        self.quantity = quantity
        self.expiry_date = expiry_date

    def is_expired(self):
        return datetime.now().date() > self.expiry_date

