from abc import ABC, abstractmethod

# Abstract class (Abstraction)
class BankAccount(ABC):

    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance   # Encapsulation

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def get_balance(self):
        return self.__balance

    @abstractmethod
    def withdraw(self, amount):
        pass


# Inheritance
class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        if amount <= self.get_balance():
            print("Savings Account Withdrawal:", amount)
        else:
            print("Savings Account: Insufficient balance")


class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        overdraft = 5000

        if amount <= self.get_balance() + overdraft:
            print("Current Account Withdrawal:", amount)
        else:
            print("Current Account: Overdraft limit exceeded")


accounts = []

# n inputs
n = int(input("Enter number of accounts: "))

for i in range(n):

    print("\nEnter details for account", i+1)

    name = input("Enter name: ")
    acc_no = int(input("Enter account number: "))
    balance = float(input("Enter initial balance: "))

    acc_type = input("Enter account type (savings/current): ").lower()

    if acc_type == "savings":
        acc = SavingsAccount(name, acc_no, balance)
    else:
        acc = CurrentAccount(name, acc_no, balance)

    accounts.append(acc)


# Polymorphism demonstration
print("\n--- Polymorphism Demonstration ---")

for acc in accounts:

    print("\nAccount Holder:", acc.name)

    deposit_amount = float(input("Enter deposit amount: "))
    acc.deposit(deposit_amount)

    withdraw_amount = float(input("Enter withdraw amount: "))

    # Same method call, different behavior
    acc.withdraw(withdraw_amount)

    print("Current Balance:", acc.get_balance())