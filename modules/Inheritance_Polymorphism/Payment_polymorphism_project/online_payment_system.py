# Real-time Project: Online Payment System

# ---------------------------
# (a) Method Overriding
# ---------------------------

class Payment:

    def pay(self, amount):
        print("Processing payment of", amount)


class CreditCardPayment(Payment):

    def pay(self, amount):   # overriding
        print("Paid", amount, "using Credit Card")


class UPIPayment(Payment):

    def pay(self, amount):   # overriding
        print("Paid", amount, "using UPI")


class CashPayment(Payment):

    def pay(self, amount):   # overriding
        print("Paid", amount, "using Cash")


# ---------------------------
# (b) Duck Typing
# ---------------------------

class PhonePay:

    def transaction(self):
        print("Transaction via PhonePe")


class GooglePay:

    def transaction(self):
        print("Transaction via Google Pay")


def make_transaction(app):
    app.transaction()


# ---------------------------
# (c) Operator Overloading
# ---------------------------

class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return self.amount + other.amount


# ---------------------------
# (d) Method Overloading
# ---------------------------

class Calculator:

    def total(self, *amounts):
        return sum(amounts)


# ---------------------------
# Main Program
# ---------------------------

amount = int(input("Enter payment amount: "))

p1 = CreditCardPayment()
p2 = UPIPayment()
p3 = CashPayment()

print("\n--- Payment Methods ---")
p1.pay(amount)
p2.pay(amount)
p3.pay(amount)


print("\n--- Duck Typing Example ---")
app1 = PhonePay()
app2 = GooglePay()

make_transaction(app1)
make_transaction(app2)


print("\n--- Operator Overloading Example ---")
b1 = Bill(200)
b2 = Bill(300)

print("Total Bill:", b1 + b2)


print("\n--- Method Overloading Example ---")
c = Calculator()

print("Total Payment:", c.total(100, 200))
print("Total Payment:", c.total(100, 200, 300))