# Nested dictionary to store student data
students = {}

# Function to add a student
def add_student():
    name = input("Enter student name: ")
    subjects = int(input("Enter number of subjects: "))

    marks_dict = {}

    for i in range(subjects):
        subject = input("Enter subject name: ")
        marks = float(input("Enter marks: "))
        marks_dict[subject] = marks

    students[name] = marks_dict
    print("Student added successfully!\n")


# Function to update marks
def update_marks():
    name = input("Enter student name to update: ")

    if name in students:
        subject = input("Enter subject to update: ")

        if subject in students[name]:
            new_marks = float(input("Enter new marks: "))
            students[name][subject] = new_marks
            print("Marks updated successfully!\n")
        else:
            print("Subject not found!\n")
    else:
        print("Student not found!\n")


# Function to calculate GPA
def calculate_gpa(name):
    if name in students:
        total = sum(students[name].values())
        count = len(students[name])
        gpa = total / count
        return gpa
    else:
        return None


# Function to display all records
def display_records():
    if not students:
        print("No records available\n")
        return

    for name, subjects in students.items():
        print("\nStudent:", name)

        for subject, marks in subjects.items():
            print(subject, ":", marks)

        gpa = calculate_gpa(name)
        print("GPA:", round(gpa, 2))


# Main menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Display Records")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        update_marks()

    elif choice == "3":
        display_records()

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.\n")