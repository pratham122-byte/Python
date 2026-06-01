class Student:
    def _int_(self,name,marks):
        self.name = name
        self.marks = marks
    def get_name(self):
        return self.name
    def get_marks(self):
        return self.marks
    def set_marks(self,marks):
        if 0<=marks<=100:
            self.marks = marks
        else:
            print("Invalid marks")
s=Student("john",85)
print(s.get_name())
print(s.get_marks())
s.set_marks(95)
print(s.get_marks())
s.get_marks(())