import re
import os

folder = "secure_text_processor"

# File paths
input_file = os.path.join(folder, "input_data.txt")
code_file = os.path.join(folder, "python_code.py")

# Read files
with open(input_file, "r") as f:
    text = f.read()

with open(code_file, "r") as f:
    code = f.read()

print("===== SECURE TEXT PROCESSOR =====\n")

# --------------------------------------------------
# (a) camelCase → snake_case (Customer Name)
# --------------------------------------------------
camel = re.search(r"CustomerName:\s*(\w+)", text)
if camel:
    name = camel.group(1)
    snake = re.sub(r'([a-z])([A-Z])', r'\1_\2', name).lower()
    print("Converted Name:", snake)

print("-" * 50)

# --------------------------------------------------
# (b) Remove extra whitespace
# --------------------------------------------------
clean_text = re.sub(r'\s+', ' ', text)
print("\nCleaned Text:\n", clean_text)

print("-" * 50)

# --------------------------------------------------
# (c) Mask Credit Card Numbers
# --------------------------------------------------
masked = re.sub(r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?(\d{4})\b',
                r'****-****-****-\1', text)

print("\nMasked Data:\n", masked)

print("-" * 50)

# --------------------------------------------------
# (d) Extract Function Names
# --------------------------------------------------
functions = re.findall(r'def\s+([a-zA-Z_]\w*)\s*\(', code)

print("\nFunctions Found:", functions)

print("-" * 50)

# --------------------------------------------------
# (e) Convert Dates MM/DD/YYYY → DD-MM-YYYY
# --------------------------------------------------
converted_dates = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\2-\1-\3', text)

print("\nConverted Dates:\n", converted_dates)

print("-" * 50)

print("\n===== PROCESS COMPLETE =====")