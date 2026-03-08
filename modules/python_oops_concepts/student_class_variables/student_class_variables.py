# Class definition
class Student:
    
    # Class variable (common for all objects)
    school_name = "ABC Public School"
    
    # Constructor to initialize instance variables
    def __init__(self, name, roll_no, marks):
        self.name = name          # Instance variable
        self.roll_no = roll_no    # Instance variable
        self.marks = marks        # Instance variable
    
    # Method to display student details
    def display_info(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print("School Name:", Student.school_name)
        print("----------------------")


# Creating objects with user input
n = int(input("Enter number of students: "))  # input for number of objects

students = []

for i in range(n):
    print("\nEnter details for Student", i+1)
    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter marks: "))
    
    s = Student(name, roll_no, marks)
    students.append(s)


print("\nStudent Details:")
for s in students:
    s.display_info()


# Changing class variable
Student.school_name = "XYZ International School"

print("\nAfter changing school name (class variable):")
for s in students:
    s.display_info()