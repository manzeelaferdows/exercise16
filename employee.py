from person import Person

class Employee(Person):
    def __init__(self, name, gender, work_department):
        super().__init__(name, gender)
        self._work_department = work_department

    def __str__(self):
        return "Name: " + self._name + "\nGender: " + self._gender + "\nDepartment: " + self._work_department
