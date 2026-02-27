"""
Scenario: Banking System - Customer ID Lookup
"""

def linear_search(customer_ids, target_id):
    for i in range(len(customer_ids)):
        if customer_ids[i] == target_id:
            return i
    return -1


# Customer database (unsorted)
customer_ids = [1054, 1098, 1021, 1102, 1080]

search_id = 1098

result = linear_search(customer_ids, search_id)

if result != -1:
    print("Customer found at index:", result)
else:
    print("Customer ID not found")