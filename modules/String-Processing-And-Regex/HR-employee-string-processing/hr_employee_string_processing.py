"""
Processes multiple employee records using Python string methods.
"""

def process_employee(employee_name, employee_id, department_code, salary, email, report_title):

    print("\n" + "=" * 60)
    print("EMPLOYEE REPORT".center(60))
    print("=" * 60)

    # 1. upper()
    print("Department (Uppercase):", department_code.upper())

    # 2. lower()
    print("Email (Lowercase):", email.lower())

    # 3. strip()
    clean_name = employee_name.strip()
    print("Clean Name:", clean_name)

    # 4. split()
    print("Name Parts:", clean_name.split())

    # 5. join()
    print("Employee Code:", "_".join(clean_name.split()))

    # 6. replace()
    print("Updated Email Domain:", email.replace("company.com", "corporate.com"))

    # 7. find()
    print("Position of '@' in Email:", email.find("@"))

    # 8. count()
    print("Dot Count in Email:", email.count("."))

    # 9. startswith()
    print("Valid Employee ID Prefix:", employee_id.startswith("emp"))

    # 10. endswith()
    print("Valid Company Email:", email.endswith("company.com"))

    # 11. isdigit()
    print("Valid Salary (Numeric):", salary.isdigit())

    # 12. isalpha()
    print("Valid Department Name:", department_code.isalpha())

    # 13. isalnum()
    print("Valid Employee ID Format:", employee_id.isalnum())

    # 14. center()
    print(report_title.upper().center(60, "-"))

    # 15. zfill()
    print("Formatted Employee Number:", employee_id[-3:].zfill(5))

    # 16. encode()
    print("Encoded Confidential Tag:", "Confidential".encode())

    # 17. title()
    print("Proper Name Format:", clean_name.title())

    # 18. swapcase()
    print("Swapcase Department:", department_code.swapcase())

    print("=" * 60)


# ---------------- MAIN PROGRAM ----------------

num = int(input("Enter number of employees: "))

for i in range(num):
    print(f"\nEnter details for Employee {i+1}")

    employee_name = input("Employee Name: ")
    employee_id = input("Employee ID (e.g., emp2025001): ")
    department_code = input("Department Code: ")
    salary = input("Salary: ")
    email = input("Email: ")
    report_title = input("Report Title: ")

    process_employee(employee_name, employee_id, department_code, salary, email, report_title)
# 8️⃣ replace() – Update company domain
print("8. replace():", email.replace("company.com", "corporate.com"))


# 9️⃣ find() – Find domain position
print("9. find():", email.find("@"))


# 🔟 count() – Count dots in email
print("10. count():", email.count("."))


# 1️⃣1️⃣ startswith() – Validate employee ID prefix
print("11. startswith():", employee_id.startswith("emp"))


# 1️⃣2️⃣ endswith() – Check company email domain
print("12. endswith():", email.endswith("company.com"))


# 1️⃣3️⃣ isdigit() – Validate salary input
print("13. isdigit():", salary.isdigit())


# 1️⃣4️⃣ isalpha() – Validate department name
print("14. isalpha():", department_code.isalpha())


# 1️⃣5️⃣ isalnum() – Check employee ID format
print("15. isalnum():", employee_id.isalnum())


# 1️⃣6️⃣ center() – Format HR report heading
print("16. center():", report_title.upper().center(50, "="))


# 1️⃣7️⃣ zfill() – Format employee number
print("17. zfill():", "45".zfill(5))  
# 00045


# 1️⃣8️⃣ encode() – Encode confidential data
print("18. encode():", "Confidential".encode())


# 1️⃣9️⃣ title() – Proper name formatting
print("19. title():", employee_name.strip().title())


# 2️⃣0️⃣ swapcase() – Audit case transformation
print("20. swapcase():", "Hr DePaRtMeNt".swapcase())