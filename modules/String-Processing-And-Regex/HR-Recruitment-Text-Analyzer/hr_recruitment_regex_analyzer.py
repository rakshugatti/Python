"""
Demonstrates real-world regex operations for validating,
extracting, masking, and analyzing HR recruitment data.
"""

import re


# (a) Validate Email Address
def validate_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    if re.match(pattern, email):
        return "Valid Email"
    else:
        return "Invalid Email"


# (b) Extract Phone Numbers (10-digit format)
def extract_phone_numbers(text):
    pattern = r'\b\d{10}\b'
    return re.findall(pattern, text)


# (c) Replace All Digits with '#'
def mask_digits(text):
    return re.sub(r'\d', '#', text)


# (d) Split Sentence by Multiple Delimiters
def split_text(text):
    pattern = r'[,\.;|:\s]+'
    return re.split(pattern, text)


# (e) Find Words Starting with Capital Letter
def find_capital_words(text):
    pattern = r'\b[A-Z][a-z]*\b'
    return re.findall(pattern, text)


# ---------------- MAIN PROGRAM ----------------

print("\n=== HR Recruitment Regex Analyzer ===\n")
num_candidates = int(input("Enter number of candidates to analyze: "))
for i in range(1,num_candidates+1):
    print(f"\n---Processing Candidate {i} ---\n")
    name=input("Enter candidate name: ")
    email_input = input("Enter candidate email: ")
    phone_number = input("Enter candidate phone number: ")
    location = input("Enter candidate location: ")  
    department = input("Enter candidate department: ")  
    sample_text = f"Name: {name}, Email: {email_input}, Phone: {phone_number}, Location: {location}, Department: {department}"
    print("\n1. Email Validation Result:", validate_email(email_input))
    print("2. Extracted Phone Numbers:", extract_phone_numbers(sample_text))
    print("3. Masked Text:\n", mask_digits(sample_text))
    print("4. Split Text:", split_text(sample_text))
    print("5. Capitalized Words:", find_capital_words(sample_text))
print("\n===Processing Completed Successfully===\n")