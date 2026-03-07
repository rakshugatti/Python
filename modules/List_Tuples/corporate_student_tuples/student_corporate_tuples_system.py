from collections import namedtuple

print("---- Campus Placement System ----")

# Number of students entering corporate field
n = int(input("Enter number of placed students: "))

students = []

# (a) Tuple Packing
for i in range(n):
    name = input("Enter student name: ")
    role = input("Enter job role: ")
    department = input("Enter department: ")

    student = (name, role, department)  # tuple packing
    students.append(student)

print("\nStudent Placement Records:")
for s in students:
    # (a) Tuple Unpacking
    name, role, dept = s
    print("Name:", name, "| Role:", role, "| Department:", dept)


# (b) Swapping two students
print("\n---- Swapping Project Assignments ----")
if len(students) >= 2:
    student1 = students[0]
    student2 = students[1]

    print("Before Swap:", student1[0], "and", student2[0])

    student1, student2 = student2, student1

    print("After Swap:", student1[0], "and", student2[0])


# (c) Function returning multiple values using tuple
print("\n---- Salary Calculation ----")

def salary_details(base_salary, bonus):
    total = base_salary + bonus
    return base_salary, bonus, total

base, bonus, total = salary_details(50000, 5000)

print("Base Salary:", base)
print("Bonus:", bonus)
print("Total Salary:", total)


# (d) Using tuples as dictionary keys (office seat allocation)
print("\n---- Office Seat Allocation ----")

office_seats = {
    (1, 101): "Software Engineer",
    (1, 102): "Data Analyst",
    (2, 201): "System Engineer"
}

print("Seat (1,102) assigned to role:", office_seats[(1,102)])


# (e) Named Tuple for employee record
print("\n---- Named Tuple Example ----")

Employee = namedtuple("Employee", ["name", "employee_id", "role"])

emp1 = Employee("Aman", 1001, "Software Engineer")

print("Employee Name:", emp1.name)
print("Employee ID:", emp1.employee_id)
print("Employee Role:", emp1.role)