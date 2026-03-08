balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Withdrawn:", amount)
    else:
        print("Insufficient balance")

def check_balance():
    print("Current Balance:", balance)


# Demo
deposit(500)
withdraw(200)
check_balance()