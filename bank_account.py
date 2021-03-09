class Account:
    # numCreated = 0
    def __init__(self, initial_balance):
        # self._account_type = account_type
        self._balance = initial_balance
        # numCreated += 1

    def withdrawn(self, amount):
        self._balance -= amount
        return self._balance

class Saving_Account(Account):
    def __init__(self, initial_balance):
        super().__init__(initial_balance)

    def deposit(self, amount):
        self._balance += amount
        return self._balance



    # def getbalance(self):
    #     return self._balance