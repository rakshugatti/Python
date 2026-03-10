class Employee:

    # Constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        print("Constructor called for", self.name)

    # Instance Method - display
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)

    # Instance Method - appraise
    def appraise(self, percent):
        self.salary = self.salary + (self.salary * percent / 100)
        print("New Salary after appraisal:", self.salary)

    # Class Method
    @classmethod
    def from_string(cls, emp_string):
        name, age, salary = emp_string.split("-")
        return cls(name, int(age), float(salary))

    # Static Method
    @staticmethod
    def is_valid_salary(salary):
        if salary > 0:
            return True
        else:
            return False

    # Destructor
    def __del__(self):
        print("Destructor called. Employee object deleted:", self.name)


# -------- Demonstration --------

# Creating object using constructor
emp1 = Employee("Rahul", 25, 40000)

print("\nDisplay Employee Details")
emp1.display()

print("\nAppraisal")
emp1.appraise(10)

# Creating object using class method
emp2 = Employee.from_string("Anita-28-50000")

print("\nSecond Employee Details")
emp2.display()

# Using static method
print("\nSalary Validity Check")
print(Employee.is_valid_salary(50000))

# Deleting object to show destructor
del emp1