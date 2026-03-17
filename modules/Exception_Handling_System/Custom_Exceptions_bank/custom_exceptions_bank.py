# Base Exception
class BankingError(Exception):
    pass


# Custom Exceptions
class InsufficientFundsError(BankingError):
    pass


class InvalidAccountError(BankingError):
    pass


class TransactionLimitExceeded(BankingError):
    pass


# Bank Account Class
class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        # Check account validity
        if self.account_number != "12345":
            raise InvalidAccountError("Invalid Account Number")

        # Check transaction limit
        if amount > 10000:
            raise TransactionLimitExceeded("Transaction limit exceeded (Max ₹10000)")

        # Check sufficient balance
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient balance")

        # If all valid
        self.balance -= amount
        print(f"Withdrawal Successful! Remaining Balance: ₹{self.balance}")


# Main Program
try:
    acc_no = input("Enter Account Number: ")
    balance = float(input("Enter Balance: "))
    amount = float(input("Enter Withdrawal Amount: "))

    account = BankAccount(acc_no, balance)
    account.withdraw(amount)

# Handling custom exceptions
except InvalidAccountError as e:
    print("Error:", e)

except TransactionLimitExceeded as e:
    print("Error:", e)

except InsufficientFundsError as e:
    print("Error:", e)

except BankingError as e:
    print("Banking Error:", e)

except Exception as e:
    print("Unexpected Error:", e)