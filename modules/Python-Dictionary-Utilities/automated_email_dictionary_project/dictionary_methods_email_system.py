# This program demonstrates all important Python dictionary methods
# using a real-time example of generating employee email IDs.

# Taking number of employees as input
n = int(input("Enter number of employees: "))

# Creating an empty dictionary to store employee emails
employees = {}

# Loop to take employee names and generate email IDs automatically
for i in range(n):
    name = input("Enter employee name: ")
    employees[name] = name.lower() + "@company.com"

# Display the dictionary
print("\nGenerated Employee Emails:")
print(employees)


# -------------------------------
# 1. get() method
# Used to safely get value of a key
# -------------------------------
search = input("\nEnter employee name to search email: ")
print("Email:", employees.get(search, "Employee not found"))


# -------------------------------
# 2. keys() method
# Displays all keys in dictionary
# -------------------------------
print("\nEmployee Names:")
print(employees.keys())


# -------------------------------
# 3. values() method
# Displays all values in dictionary
# -------------------------------
print("\nEmployee Email IDs:")
print(employees.values())


# -------------------------------
# 4. items() method
# Displays key-value pairs
# -------------------------------
print("\nEmployee Name and Email:")
for name, email in employees.items():
    print(name, ":", email)


# -------------------------------
# 5. update() method
# Used to add or update dictionary data
# -------------------------------
new_name = input("\nEnter new employee name to add: ")
employees.update({new_name: new_name.lower() + "@company.com"})
print("Updated Dictionary:", employees)


# -------------------------------
# 6. pop() method
# Removes specific key from dictionary
# -------------------------------
remove_name = input("\nEnter employee name to remove: ")
employees.pop(remove_name, "Employee not found")
print("Dictionary after pop:", employees)


# -------------------------------
# 7. popitem() method
# Removes last inserted item
# -------------------------------
print("\nRemoving last inserted employee using popitem()")
employees.popitem()
print("Dictionary after popitem:", employees)


# -------------------------------
# 8. setdefault() method
# Adds key if it does not exist
# -------------------------------
employees.setdefault("admin", "admin@company.com")
print("\nDictionary after setdefault():")
print(employees)


# -------------------------------
# 9. copy() method
# Creates a duplicate dictionary
# -------------------------------
backup_employees = employees.copy()
print("\nBackup Dictionary:")
print(backup_employees)



# 10. fromkeys() method
# Creates new dictionary with default value

names = list(employees.keys())
email_status = dict.fromkeys(names, "Pending")
print("\nEmail Sending Status:")
print(email_status)


# -------------------------------
# 11. clear() method
# Removes all items from dictionary
# -------------------------------
backup_employees.clear()
print("\nBackup Dictionary after clear():")
print(backup_employees)