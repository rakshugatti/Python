# Employee File Handling System

print("\n--- Company Employee Record System ---\n")

# (a) Create & Write to file
file = open("employees.txt", "w")
file.write("101,John,Manager\n")
file.write("102,Alice,Developer\n")
file.write("103,Bob,Tester\n")
file.close()
print("✅ Employee data written to file")

print("\n-----------------------------")

# (b) Read using read()
file = open("employees.txt", "r")
print("📄 read():")
print(file.read())
file.close()

print("\n-----------------------------")

# Read using readline()
file = open("employees.txt", "r")
print("📄 readline():")
print(file.readline())
file.close()

print("\n-----------------------------")

# Read using readlines()
file = open("employees.txt", "r")
print("📄 readlines():")
print(file.readlines())
file.close()

print("\n-----------------------------")

# (c) Append new employee
with open("employees.txt", "a") as file:
    file.write("104,David,HR\n")
print("✅ New employee added")

print("\n-----------------------------")

# (d) Using 'with' (auto close)
with open("employees.txt", "r") as file:
    print("📄 Using with statement:")
    print(file.read())

print("\n-----------------------------")

# (e) Binary Mode (backup file)
with open("employees_backup.bin", "wb") as file:
    file.write(b"Backup of employee data")
print("✅ Binary file created")

with open("employees_backup.bin", "rb") as file:
    print("📄 Binary Read:", file.read())

print("\n--- System Completed ---")