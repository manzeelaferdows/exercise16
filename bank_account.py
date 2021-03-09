class Account:
    def __init__(self, initial_balance):
        self._balance = initial_balance

    def withdrawn(self, amount):
        if amount > 0:
            check_balance = self._balance - amount
            if check_balance < 0:
                return f"Withdrawal unsuccessful - the maximum amount you can withdraw is {self._balance}"
            else:
                self._balance = amount
                return f"Withdrawal successful"
        self._balance -= amount
        return self._balance

    @property
    def balance(self):
        return self._balance

