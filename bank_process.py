from bank_account import Account
from bank_account import Saving_Account

joint_account = Account(1000)
savings_account = Saving_Account(50)

print(joint_account._withdrawn(10))


print(joint_account)
print(savings_account)


