# Dictionary Comprehension Example 1
# Automatically generate email IDs for employees

n = int(input("Enter number of employees: "))

names = []

# Taking employee names
for i in range(n):
    name = input("Enter employee name: ")
    names.append(name)

# Dictionary comprehension to generate emails
emails = {name: name.lower() + "@company.com" for name in names}

print("\nGenerated Email IDs:")
print(emails)