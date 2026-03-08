# Dictionary Comprehension Example 2
# Generate bonus report for employees

n = int(input("Enter number of employees: "))

salary = {}

# Taking employee salary details
for i in range(n):
    name = input("Enter employee name: ")
    sal = int(input("Enter salary: "))
    salary[name] = sal

# Bonus calculation using dictionary comprehension
bonus = {name: sal * 0.10 for name, sal in salary.items()}

print("\nEmployee Bonus Report:")
print(bonus)