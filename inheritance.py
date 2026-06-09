class pr:
    def func1(self):
        print("this function is in parent class")
    def func3(self):
        print("hello")
class ch(pr):
    def func2(self):
        print("this function is in child class")
ob=ch()
ob.func1()
ob.func2()
ob.func3()