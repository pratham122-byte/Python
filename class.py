class Student:
    schl_name = "Amity University"

    def _init_(self,name,age):
        self.name=name
        self.age=age

    def printboth(self):
        return f"my name is {self.name} and i am studying in {Student.schl_name} and i am {self.age} years old"
    

##modify school name

Student.schl_name = "AIIT"
    
s1 = Student("pratham",22)
s1.printboth()
