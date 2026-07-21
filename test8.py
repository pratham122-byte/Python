class student:
    def __init__(self, name,roll_no):
        self.name = name
        self.roll_no = roll_no
class ugstudent(student):
    def __init__(self, name, roll_no):
        super().__init__(name, roll_no)
    def display(self):
        print("UG Student Details:")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
class pgstudent(ugstudent):
    def __init__(self,name,roll_no):
        super().__init__(name,roll_no)
    def display(self):
        print("PG Student Details:")
        print("name:",self.name)
        print("roll no:",self.roll_no)
a=pgstudent("pratham",104)
a.display()
b=pgstudent("rahul",203)
b.display()
c=pgstudent("sneha",305)
c.display()
d=pgstudent("anita",407)
d.display()
e=ugstudent("pratham",104)
e.display()
f=ugstudent("rahul",203)
f.display()
h=ugstudent("sneha",305)
h.display()
j=ugstudent("anita",407)
j.display()
