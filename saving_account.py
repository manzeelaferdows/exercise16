from bank_account_types import Account

class Saving_Account(Account):
    # def __init__(self,):
    #     # super().__init__(amount)

    def deposit(self, amount):
        self._balance += amount
        return