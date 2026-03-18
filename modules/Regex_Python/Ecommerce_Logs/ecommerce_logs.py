import re

# --- Step 1: Input log entries from user ---
print("Enter log entries (type 'END' on a new line to finish):")
lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

log_text = "\n".join(lines)
print("\n--- Log Text ---")
print(log_text)

# --- Step 2: Apply all regex operations ---

# 1. match() - check if the log starts with OrderID
match_result = re.match(r"OrderID:\s\d+", log_text)
print("\n1. match():")
if match_result:
    print("First line starts with:", match_result.group())
else:
    print("No match at the start")

# 2. search() - find the first email anywhere
search_result = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", log_text)
print("\n2. search():")
if search_result:
    print("First email found:", search_result.group())
else:
    print("No email found")

# 3. findall() - extract all order IDs
all_orders = re.findall(r"OrderID:\s(\d+)", log_text)
print("\n3. findall():")
print("All Order IDs:", all_orders)

# 4. finditer() - find all emails with positions
print("\n4. finditer():")
for m in re.finditer(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", log_text):
    print(m.group(), "at position", m.start())

# 5. sub() - mask all emails for privacy
masked_text = re.sub(r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-z]{2,})", r"\1@*****", log_text)
print("\n5. sub():")
print(masked_text)

# 6. split() - split log entries into separate lines
split_logs = re.split(r"\n+", log_text.strip())
print("\n6. split():")
print(split_logs)

# 7. compile() - find completed orders
completed_pattern = re.compile(r"OrderID:\s(\d+),.*Status:\sCompleted")
completed_orders = completed_pattern.findall(log_text)
print("\n7. compile():")
print("Completed Orders:", completed_orders)
""" Type the input as:OrderID: 12345, Customer: Alice, Email: alice@example.com, Status: Completed
OrderID: 12346, Customer: Bob, Email: bob123@gmail.com, Status: Pending
OrderID: 12347, Customer: Charlie, Email: charlie@example.com, Status: Completed
END"""