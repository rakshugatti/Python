import re
import os

# --- Folder & File ---
folder = "Security_analyzer"
file = "logs.txt"
path = os.path.join(folder, file)

# --- Read file ---
with open(path, "r") as f:
    text = f.read()

print("===== REAL-TIME REGEX ANALYZER =====\n")

# --------------------------------------------------
# (a) Greedy vs Lazy (HTML Extraction)
# --------------------------------------------------
print("1. HTML Extraction (Greedy vs Lazy)\n")

greedy_html = re.findall(r"<div>.*</div>", text)
lazy_html = re.findall(r"<div>.*?</div>", text)

print("Greedy:", greedy_html)
print("Lazy:", lazy_html)

print("-" * 50)

# --------------------------------------------------
# (b) Min vs Max Repetition
# --------------------------------------------------
print("\n2. Min vs Max Repetition\n")

max_rep = re.findall(r"a+", text)
min_rep = re.findall(r"a+?", text)

print("Max (a+):", max_rep)
print("Min (a+?):", min_rep)

print("-" * 50)

# --------------------------------------------------
# (c) .* vs .*?
# --------------------------------------------------
print("\n3. Difference between .* and .*?\n")

greedy_match = re.search(r"Start.*End", text)
lazy_match = re.search(r"Start.*?End", text)

print("Greedy (.*):", greedy_match.group() if greedy_match else "No match")
print("Lazy (.*?):", lazy_match.group() if lazy_match else "No match")

print("-" * 50)

# --------------------------------------------------
# (d) Lookahead (?=...)
# --------------------------------------------------
print("\n4. Lookahead (?=USD)\n")

lookahead = re.findall(r"\d+(?=USD)", text)
print("Numbers followed by USD:", lookahead)

print("-" * 50)

# --------------------------------------------------
# (e) Lookbehind (?<=₹)
# --------------------------------------------------
print("\n5. Lookbehind (?<=₹)\n")

lookbehind = re.findall(r"(?<=₹)\d+", text)
print("Numbers after ₹:", lookbehind)

print("-" * 50)

print("\n===== ANALYSIS COMPLETE =====")