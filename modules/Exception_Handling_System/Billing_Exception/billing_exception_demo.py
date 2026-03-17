try:
    print("---- Billing System ----")

    # User input
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    # Calculation
    total = quantity * price

    # Risk of division error
    discount_percent = float(input("Enter discount percentage: "))
    discount = total / discount_percent

    # File handling (discount file)
    file = open("discount.txt", "r")
    extra_discount = float(file.read())

    final_amount = total - discount - extra_discount

# Specific exceptions
except ValueError:
    print("Invalid input! Please enter numeric values.")

except ZeroDivisionError:
    print("Discount percentage cannot be zero.")

except FileNotFoundError:
    print("Discount file not found.")

# Multiple exceptions
except (TypeError, IndexError) as e:
    print("Multiple error occurred:", e)

# Catch all exceptions
except Exception as e:
    print("Unexpected error:", e)

# Runs only if no exception
else:
    print("\nTotal Amount:", total)
    print("Final Amount after discount:", final_amount)

# Always executes
finally:
    print("\nThank you for using Billing System!")