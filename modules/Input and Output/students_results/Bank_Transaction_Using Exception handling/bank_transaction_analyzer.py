# bank_transaction_analyzer.py

try:
    # Step 1: Take comma-separated transaction amounts
    user_input = input("Enter daily transaction amounts (comma-separated): ")

    # Step 2: Split input into list
    transactions = user_input.split(",")

    # Step 3: Convert each transaction to float (banking uses decimals)
    amounts = []
    for transaction in transactions:
        amounts.append(float(transaction.strip()))

    # Step 4: Calculate banking statistics
    total_amount = sum(amounts)
    average_amount = total_amount / len(amounts)
    highest_transaction = max(amounts)
    lowest_transaction = min(amounts)

    # Step 5: Display results
    print("\n----- Daily Transaction Summary -----")
    print("Transactions:", amounts)
    print("Total Amount: ₹", total_amount)
    print("Average Transaction: ₹", average_amount)
    print("Highest Transaction: ₹", highest_transaction)
    print("Lowest Transaction: ₹", lowest_transaction)

except ValueError:
    print("Error: Please enter only numeric transaction amounts separated by commas.")

except ZeroDivisionError:
    print("Error: No transaction data entered.")