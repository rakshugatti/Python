# File: student_records_program.py

students = []

# number of inputs
n = int(input("Enter number of students: "))

# taking n student records
for i in range(n):

    print("\nEnter details for student", i+1)

    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))

    # store record as tuple
    record = (name, roll, marks)
    students.append(record)


# (a) Sort by marks in descending order
sorted_students = sorted(students, key=lambda x: x[2], reverse=True)


# (b) Find topper
topper = sorted_students[0]


# (c) Calculate average marks
total = 0
for s in students:
    total += s[2]

average = total / n


# students above average
above_average = []

for s in students:
    if s[2] > average:
        above_average.append(s)


# (d) Group students by grade
grades = {}

for s in students:

    marks = s[2]

    if marks >= 90:
        grade = 'A'
    elif marks >= 75:
        grade = 'B'
    elif marks >= 60:
        grade = 'C'
    else:
        grade = 'D'

    if grade not in grades:
        grades[grade] = []

    grades[grade].append(s)


# (e) Display formatted table
print("\nSTUDENT RECORD TABLE")
print("+-------------------------------------+")
print("| Name        | Roll No | Marks       |")
print("+-------------------------------------+")

for s in students:
    print(f"| {s[0]:<11} | {s[1]:<7} | {s[2]:<10} |")

print("+-------------------------------------+")


# Display sorted students
print("\nStudents sorted by marks (Descending):")
for s in sorted_students:
    print(s)


# Display topper
print("\nTopper:")
print(topper)


# Display average
print("\nAverage Marks:", average)


# Students above average
print("\nStudents scoring above average:")
for s in above_average:
    print(s)


# Students grouped by grade
print("\nStudents grouped by grade:")

for g in grades:
    print("Grade", g, ":", grades[g])