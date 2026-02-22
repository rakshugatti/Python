# employee_report_formatter_multi_input.py

from string import Template

employees = []

# Ask how many employees to add
num = int(input("Enter number of employees: "))

for i in range(num):
    print(f"\nEnter details for Employee {i+1}")

    emp_id = int(input("Employee ID: "))
    name = input("Name: ")
    department = input("Department: ")
    salary = float(input("Salary: "))
    rating = float(input("Performance Rating: "))

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary,
        "rating": rating
    }

    employees.append(employee)

print("\n========== Employee Performance Reports ==========\n")

for employee in employees:

    print("--------------------------------------------")
    print(f"Processing Employee ID: {employee['id']}\n")

    # 1️⃣ String Concatenation
    report1 = "Employee: " + employee["name"] + \
              ", Department: " + employee["department"] + \
              ", Salary: " + str(employee["salary"])
    print("1. Concatenation:")
    print(report1)
    print()

    # 2️⃣ % Formatting
    report2 = "Employee: %s | Dept: %s | Rating: %.1f" % (
        employee["name"],
        employee["department"],
        employee["rating"]
    )
    print("2. % Formatting:")
    print(report2)
    print()

    # 3️⃣ str.format()
    report3 = "Employee ID: {} | Salary: {:.2f}".format(
        employee["id"],
        employee["salary"]
    )
    print("3. str.format():")
    print(report3)
    print()

    # 4️⃣ f-Strings
    report4 = (
        f"Employee {employee['name']} (ID: {employee['id']}) "
        f"works in {employee['department']} with rating {employee['rating']}"
    )
    print("4. f-Strings:")
    print(report4)
    print()

    # 5️⃣ Template Strings
    email_template = Template(
        "Dear $name,\n"
        "Your performance rating is $rating.\n"
        "Keep up the good work!\n"
    )

    email_message = email_template.substitute(
        name=employee["name"],
        rating=employee["rating"]
    )

    print("5. Template String (Email Format):")
    print(email_message)

print("========== Reports Generated Successfully ==========")