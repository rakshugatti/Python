# Base Class
# -------------------------

class Person:

    def __init__(self, name):
        self.name = name
        print("Person constructor called")

    def show_details(self):
        print("Name:", self.name)


# -------------------------
# Single Inheritance
# -------------------------

class Employee(Person):

    def __init__(self, name, emp_id):
        super().__init__(name)   # calling parent constructor
        self.emp_id = emp_id
        print("Employee constructor called")

    def show_details(self):
        super().show_details()   # extending parent method
        print("Employee ID:", self.emp_id)


# -------------------------
# Multiple Inheritance
# -------------------------

class Department:

    def __init__(self, dept):
        self.dept = dept
        print("Department constructor called")

    def show_department(self):
        print("Department:", self.dept)


# -------------------------
# Diamond Problem Structure
# -------------------------

class Manager(Employee, Department):

    def __init__(self, name, emp_id, dept):
        super().__init__(name, emp_id)  # MRO handles constructor order
        Department.__init__(self, dept)
        print("Manager constructor called")

    def show_all(self):
        super().show_details()
        self.show_department()


# -------------------------
# Main Program
# -------------------------

name = input("Enter manager name: ")
emp_id = input("Enter employee ID: ")
dept = input("Enter department: ")

m = Manager(name, emp_id, dept)

print("\nEmployee Details")
m.show_all()

print("\nMethod Resolution Order:")
print(Manager.mro())