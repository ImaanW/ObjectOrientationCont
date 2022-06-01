class Account:
    balance = 0
# constructor
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amt):
        self.balance += amt
        return self.balance

    def withdraw(self, amt):
        if amt > self.balance:
            raise InsufficientFunds('Victoria is Awesome')
        else:
            self.balance -= amt

class InsufficientFunds(Exception):
    pass

