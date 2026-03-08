print("Procedural Programming Example")

balance = 1000

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
    else:
        print("Insufficient balance")

def check_balance():
    print("Balance:", balance)

deposit(500)
withdraw(200)
check_balance()


print("\nObject-Oriented Programming Example")

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Balance:", self.balance)


acc = BankAccount(1000)

acc.deposit(500)
acc.withdraw(200)
acc.check_balance()