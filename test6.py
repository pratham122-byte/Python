class BankAccount:
    def _init_(self, customer, balance=0):
        self._customer = customer   
        self._balance = balance      
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ₹{amount}")
        else:
            print("Invalid deposit amount")
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self._balance:
            print("Insufficient balance")   
        else:
            self._balance -= amount
            print(f"Withdrawn: ₹{amount}")
    def show_balance(self):
        print(f"Customer Name: {self._customer}")
        print(f"Current Balance: ₹{self._balance}")
account = BankAccount("Pratham", 5000)
account.show_balance()
account.deposit(2000)
account.withdraw(1500)
account.show_balance()