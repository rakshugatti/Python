#(a) Exception chaining
def process_payment():
    try:
        amount = float(input("Enter payment amount: "))
        fee_percent = float(input("Enter processing fee %: "))

        total = amount / fee_percent   # may cause ZeroDivisionError
        print("Payment processed:", total)

    except ZeroDivisionError as e:
        raise ValueError("Invalid fee percentage entered") from e


# (b) Re-raising exception
def validate_user():
    try:
        user_id = int(input("Enter user ID: "))  # may fail
    except ValueError:
        print("Invalid user ID format")
        raise   # re-raise same exception


# (c) Suppressing sensitive details
def secure_transaction():
    try:
        int("abc")   # internal failure
    except ValueError:
        raise Exception("Transaction failed") from None


# MAIN SYSTEM
print("\n--- Online Payment System ---")

# 1. Exception Chaining
try:
    process_payment()
except Exception as e:
    print("\nPayment Error:", e)
    print("Cause:", e.__cause__)
    print("Context:", e.__context__)

print("\n---------------------------")

# 2. Re-raising
try:
    validate_user()
except Exception as e:
    print("Re-raised Error:", e)

print("\n---------------------------")

# 3. Suppressing Context
try:
    secure_transaction()
except Exception as e:
    print("Secure Error:", e)
    print("Cause:", e.__cause__)
    print("Context:", e.__context__)

print("\n---------------------------")

# (d) Traceback info
try:
    10 / 0
except Exception as e:
    print("Traceback:", e.__traceback__)

print("\nSystem Finished")