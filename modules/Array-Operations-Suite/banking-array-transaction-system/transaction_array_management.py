"""
    This program simulates a banking transaction management system
    using Python's array module.

    Operations performed:
    - Insert new transaction
    - Delete cancelled transaction
    - Traverse transaction list
    - Search for transaction ID
"""

from array import array


def main():

    # Step 1: Create array of daily transaction IDs
    transaction_ids = array('i', [1010, 1020, 1030, 1040, 1050])

    print("Initial Transaction Records:", transaction_ids)

    # Step 2: Insert new transaction (Client made new payment)
    new_transaction = 1060
    transaction_ids.append(new_transaction)
    print("\nAfter Adding New Transaction:", transaction_ids)

    # Step 3: Delete cancelled transaction
    cancelled_transaction = 1030
    if cancelled_transaction in transaction_ids:
        transaction_ids.remove(cancelled_transaction)
        print("After Cancelling Transaction:", transaction_ids)
    else:
        print("Transaction not found for cancellation.")

    # Step 4: Traverse transactions
    print("\nTraversing All Transactions:")
    for txn in transaction_ids:
        print(f"Transaction ID: {txn}")

    # Step 5: Search for a specific transaction
    search_id = 1040
    found = False

    for index in range(len(transaction_ids)):
        if transaction_ids[index] == search_id:
            print(f"\nTransaction {search_id} found at position {index}")
            found = True
            break

    if not found:
        print("\nTransaction not found.")


if __name__ == "__main__":
    main()