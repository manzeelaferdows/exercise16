from person import Person

class Customer(Person):
    def __init__(self, name, gender, shop_department):
        super().__init__(name, gender)
        self._shop_department = shop_department

    def __str__(self):
        return "Name: " + self._name + "\nGender: " + self._gender + "\nDepartment: " + self._shop_department

