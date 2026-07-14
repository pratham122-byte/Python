class Private1:
    def _init_(self):
        self.__salary = 50000   # private variable

    def salary(self):          # public method
        return self.__salary

obj = Private1()
print(obj.salary())