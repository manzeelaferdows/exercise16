class Person:
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender.upper()

    def __str__(self):
        return "Name: " + self._name + "\nGender: " + self._gender

class Employee(Person):
    def __init__(self, name, gender, work_department):
        super().__init__(name, gender)
        self._work_department = work_department

    def __str__(self):
        return "Name: " + self._name + "\nGender: " + self._gender + "\nDepartment: " + self._work_department



class Customer(Person):
    def __init__(self, name, gender, shop_department):
        super().__init__(name, gender)
        self._shop_department = shop_department

    def __str__(self):
        return "Name: " + self._name + "\nGender: " + self._gender + "\nDepartment: " + self._shop_department



        # def display(self):
        #     print('Name:', self.name)
        #     print('Age:', self.age)

