"""
Scenario: CRM System - Remove Duplicate Client Records
"""

def remove_duplicates(client_ids):
    unique_clients = []

    for cid in client_ids:
        exists = False

        for item in unique_clients:
            if item == cid:
                exists = True
                break

        if not exists:
            unique_clients.append(cid)

    return unique_clients


client_ids = [101, 102, 103, 102, 104, 101, 105]

print("Original Client IDs:", client_ids)
print("After Cleaning:", remove_duplicates(client_ids))