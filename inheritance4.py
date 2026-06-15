class university:
    def set_university(self):
        self.university_name="Amity University"
class department(university):
    def set_department(self):
        self.dept_name="computer science"
class student(department):
    def display(self):
        print("university:",self.university_name)
        print("department:",self.dept_name)
        print("student:",self.student_name)
a=student()
a.set_university()
a.set_department()
a.student_name=input("enter the student name:")
a.display()