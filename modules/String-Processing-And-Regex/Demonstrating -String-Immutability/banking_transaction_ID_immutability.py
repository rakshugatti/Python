"""
Demonstrates why transaction IDs (strings) are immutable
and how Python creates new objects when modifications are required.
"""

# Step 1: Original Transaction ID
transaction_id = "txn2025001"

print("Original Transaction ID:", transaction_id)
print("Original Memory ID:", id(transaction_id))


# Step 2: Attempt to modify transaction ID (Security violation attempt)
try:
    transaction_id[0] = "T"   # Trying to change 't' to 'T'
except TypeError as error:
    print("\nSecurity Alert!")
    print("Error:", error)


# Step 3: Correct Way (Create New Transaction ID)
# Suppose bank upgrades format to uppercase prefix

updated_transaction_id = "T" + transaction_id[1:]

print("\nUpdated Transaction ID:", updated_transaction_id)
print("New Memory ID:", id(updated_transaction_id))


# Step 4: Verify Memory Change
print("\nMemory Changed?", id(transaction_id) != id(updated_transaction_id))