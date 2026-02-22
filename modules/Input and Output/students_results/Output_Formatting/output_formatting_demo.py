# output_formatting_demo.py

name = "Raksh"
age = 21
marks = 88.5

# 1️⃣ String Concatenation
print("1. Using Concatenation:")
print("Name: " + name + ", Age: " + str(age) + ", Marks: " + str(marks))
print()

# 2️⃣ % Formatting (Old Style)
print("2. Using % Formatting:")
print("Name: %s, Age: %d, Marks: %.1f" % (name, age, marks))
print()

# 3️⃣ str.format() Method
print("3. Using str.format():")
print("Name: {}, Age: {}, Marks: {:.1f}".format(name, age, marks))
print()

# 4️⃣ f-Strings (Recommended)
print("4. Using f-strings:")
print(f"Name: {name}, Age: {age}, Marks: {marks:.1f}")
print()

# 5️⃣ Template Strings
from string import Template

print("5. Using Template Strings:")
template = Template("Name: $name, Age: $age, Marks: $marks")
print(template.substitute(name=name, age=age, marks=marks))