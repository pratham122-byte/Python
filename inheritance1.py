class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name, self.id)


class Employee(Person):
    def print_emp(self):
        print("Employee class called")


emp1 = Employee("John", 101)
emp1.display()
emp1.print_emp()
