1. re.match()
Purpose: Checks if the pattern matches only at the start of the string.
Returns: Match object if matched; otherwise None.

import re

log_line = "OrderID: 12345, Customer: Alice"

# match() checks only at the start
match_result = re.match(r"OrderID:\s\d+", log_line)
if match_result:
    print("match():", match_result.group())

Output:

match(): OrderID: 12345

Key point: If the string started with "Customer:", match() would return None.

2. re.search()

Purpose: Searches anywhere in the string for the pattern.

Returns: Match object if found; otherwise None.

search_result = re.search(r"Customer:\s\w+", log_line)
if search_result:
    print("search():", search_result.group())

Output:

search(): Customer: Alice

Difference:

match() → only start of string

search() → anywhere in the string

3. re.findall()

Purpose: Returns all occurrences of the pattern as a list.

log_text = "OrderID: 12345, OrderID: 12346, OrderID: 12347"
order_ids = re.findall(r"OrderID:\s(\d+)", log_text)
print("findall():", order_ids)

Output:

findall(): ['12345', '12346', '12347']
4. re.finditer()

Purpose: Returns an iterator of match objects for all matches.

Useful to get positions in the text.

for m in re.finditer(r"OrderID:\s(\d+)", log_text):
    print(f"{m.group()} found at position {m.start()}")

Output:

OrderID: 12345 found at position 0
OrderID: 12346 found at position 15
OrderID: 12347 found at position 30
5. re.sub()

Purpose: Replace all occurrences of a pattern with a new string.

log_text = "Customer emails: alice@example.com, bob@gmail.com"
masked = re.sub(r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-z]{2,})", r"\1@*****", log_text)
print("sub():", masked)

Output:

sub(): Customer emails: alice@*****, bob@*****

Real-world use: Mask emails in logs for privacy compliance.

6. re.split()

Purpose: Split a string using a regex pattern.

logs = "OrderID:12345;OrderID:12346;OrderID:12347"
entries = re.split(r";", logs)
print("split():", entries)

Output:

split(): ['OrderID:12345', 'OrderID:12346', 'OrderID:12347']
7. re.compile()

Purpose: Precompile a regex for reuse, which is efficient for multiple searches.

pattern = re.compile(r"OrderID:\s(\d+),.*Status:\sCompleted")
log_text = """
OrderID: 12345, Customer: Alice, Status: Completed
OrderID: 12346, Customer: Bob, Status: Pending
OrderID: 12347, Customer: Charlie, Status: Completed
"""
completed_orders = pattern.findall(log_text)
print("compile():", completed_orders)

Output:

compile(): ['12345', '12347']