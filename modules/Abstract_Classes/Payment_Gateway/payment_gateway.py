from abc import ABC, abstractmethod


# Abstract Class
class PaymentGateway(ABC):

    @abstractmethod
    def authorize(self, amount):
        pass

    @abstractmethod
    def capture(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


# Concrete Class 1
class CreditCardPayment(PaymentGateway):

    def authorize(self, amount):
        print("Credit Card authorized for", amount)

    def capture(self, amount):
        print("Credit Card payment captured:", amount)

    def refund(self, amount):
        print("Refund processed to Credit Card:", amount)


# Concrete Class 2
class UPIPayment(PaymentGateway):

    def authorize(self, amount):
        print("UPI authorized for", amount)

    def capture(self, amount):
        print("UPI payment successful:", amount)

    def refund(self, amount):
        print("Refund sent via UPI:", amount)


# -------- Main Program --------

print("Payment System")

method = input("Enter payment method (credit/upi): ").lower()
amount = float(input("Enter amount: "))


if method == "credit":
    payment = CreditCardPayment()

elif method == "upi":
    payment = UPIPayment()

else:
    print("Invalid payment method")
    exit()


payment.authorize(amount)
payment.capture(amount)

refund_choice = input("Do you want refund? (yes/no): ").lower()

if refund_choice == "yes":
    payment.refund(amount)


# Demonstrating abstract class cannot be instantiated
print("\nTrying to create PaymentGateway object")

try:
    p = PaymentGateway()
except TypeError as e:
    print("Error:", e)