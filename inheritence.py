from PIH import Person
from PIH import Employee
from PIH import Customer

manz_person = Person('Manz', 'F')
print(manz_person)

manz_employee = Employee('Manz', 'F', 'Gaming')
print(manz_employee)

shaeera_customer = Customer('Shaeera', 'F', 'Gaming')
print(shaeera_customer)

if manz_employee._work_department == shaeera_customer._shop_department:
    print("Shopping")
