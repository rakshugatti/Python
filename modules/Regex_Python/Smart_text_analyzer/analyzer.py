import re
import os

# --- Folder and file setup ---
folder_name = "smart_text_analyzer"
file_name = "input.txt"
file_path = os.path.join(folder_name, file_name)

# --- Read text ---
with open(file_path, "r") as f:
    text = f.read()

# --- Regex patterns with named groups ---
patterns = {
    "Dates": r"(?P<date>\b\d{2}/\d{2}/\d{4}\b)",
    "IP Addresses": r"(?P<ip>\b\d{1,3}(?:\.\d{1,3}){3}\b)",
    "Hashtags": r"(?P<hashtag>#\w+)",
    "Amounts": r"(?P<amount>[₹$]\d+(?:\.\d{1,2})?)",
    "HTML Tags": r"(?P<html><[^>]+>)"
}

# --- Extract and display ---
print("===== SMART TEXT ANALYZER OUTPUT =====\n")

for key, pattern in patterns.items():
    print(f"{key}:")
    
    matches = re.finditer(pattern, text)
    found = False
    
    for m in matches:
        print(" -", m.group())
        found = True
    
    if not found:
        print(" No matches found")
    
    print("-" * 40)