# Dictionary Comprehension Example 3
# Assign report status for departments

n = int(input("Enter number of departments: "))

departments = []

# Taking department names
for i in range(n):
    dept = input("Enter department name: ")
    departments.append(dept)

# Creating dictionary with default status
report_status = {dept: "Pending" for dept in departments}

print("\nDepartment Report Status:")
print(report_status)