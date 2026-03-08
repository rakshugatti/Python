# bank_account_self_demo.py

class BankAccount:

    # constructor
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # deposit method
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Current Balance:", self.balance)

    # withdraw method
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")
        print("Current Balance:", self.balance)

    # display account info
    def display(self):
        print("\nAccount Holder:", self.name)
        print("Balance:", self.balance)


# Taking input
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

# Creating object
acc1 = BankAccount(name, balance)

# Performing operations
deposit_amount = float(input("Enter amount to deposit: "))
acc1.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
acc1.withdraw(withdraw_amount)

acc1.display()