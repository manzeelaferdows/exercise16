from person import Person
from employee import Employee
from customer import Customer

manz_person = Person('Manz', 'F')
print(manz_person)

shaeera_person = Person('Shaeera', 'F')
print(shaeera_person)

victoria_person = Person('Victoria', 'F')
print(victoria_person.get_name())

manz_employee = Employee('Manz', 'F', 'Gaming')
print(manz_employee)
print(manz_employee.get_name())
shaeera_customer = Customer('Shaeera', 'F', 'Gaming')
print(shaeera_customer)

if manz_employee._work_department == shaeera_customer._shop_department:
    print("Shopping")
