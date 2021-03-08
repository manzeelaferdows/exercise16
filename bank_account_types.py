class Account:
  # numCreated = 0
  def __init__(self, initial_balance):
      # self._account_type = account_type
      self._initial_balance = initial_balance
      # numCreated += 1
  def withdrawn(self, amount):
      self._balance -= amount
      return


