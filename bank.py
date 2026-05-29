def depoist(balance,amout):
    balance+=amout
    return balance
def withdraw(balance,amout):
    if amout > balance:
        print("insuffient balance")
    else:
        balance-=amout
    return balance
def check_balance(balance):
    print("current balance",balance)
balance=1000
balance=depoist(balance,500)
balance=withdraw(balance,200)
check_balance(balance)
