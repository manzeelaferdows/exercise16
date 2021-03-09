from bank_account import Account
from saving_account import Saving_Account

joint_account = Account(9)
savings_account = Saving_Account(50)

print(joint_account.withdrawn(10))
print(savings_account.deposit(300))


print(joint_account.balance)



