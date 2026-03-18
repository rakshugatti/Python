import re

# --- Regex Patterns ---
patterns = {
    "Mobile": r"^[6-9]\d{9}$",
    "Email": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "Password": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
    "URL": r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[\w./?=&-]*)?$",
    "PAN": r"^[A-Z]{5}[0-9]{4}[A-Z]$"
}

# --- Function to validate a single customer ---
def validate_customer(customer):
    results = {}
    for key in ["Mobile", "Email", "Password", "URL", "PAN"]:
        if re.match(patterns[key], customer[key]):
            results[key] = "Valid"
        else:
            results[key] = "Invalid"
    return results

# --- Input: Ask user for number of customers ---
n = int(input("Enter number of customers to register: "))

customers = []

for i in range(n):
    print(f"\n--- Enter details for Customer {i+1} ---")
    name = input("Name: ")
    mobile = input("Mobile (10 digits starting 6-9): ")
    email = input("Email: ")
    password = input("Password (min 8 chars, uppercase, lowercase, digit, special char): ")
    url = input("URL (http/https): ")
    pan = input("PAN (10 characters, 5 letters, 4 digits, 1 letter): ")
    
    customer = {
        "Name": name,
        "Mobile": mobile,
        "Email": email,
        "Password": password,
        "URL": url,
        "PAN": pan
    }
    
    customers.append(customer)

# --- Validation and Output ---
print("\n=== Customer Registration Validation Results ===\n")
for customer in customers:
    print(f"Customer: {customer['Name']}")
    results = validate_customer(customer)
    for field, status in results.items():
        print(f"{field}: {status}")
    print("-" * 50)