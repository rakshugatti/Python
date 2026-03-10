class Employee:

    def __init__(self, name, department, salary):
        self.name = name              # Public
        self._department = department # Protected
        self.__salary = salary        # Private

    # Getter using @property
    @property
    def salary(self):
        return self.__salary

    # Setter using @property
    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            print("Invalid salary")

    def display(self):
        print("Name:", self.name)
        print("Department:", self._department)
        print("Salary:", self.__salary)


# -------- Demonstration --------

n = int(input("Enter number of employees: "))
employees = []

for i in range(n):
    print("\nEnter details for Employee", i+1)

    name = input("Enter name: ")
    dept = input("Enter department: ")
    salary = int(input("Enter salary: "))

    emp = Employee(name, dept, salary)
    employees.append(emp)


print("\nEmployee Details")

for emp in employees:

    # Public
    print("\nPublic attribute:", emp.name)

    # Protected
    print("Protected attribute:", emp._department)

    # Private using name mangling
    print("Private attribute using name mangling:", emp._Employee__salary)

    # Getter
    print("Salary using getter:", emp.salary)

    # Setter
    new_salary = int(input("Enter updated salary: "))
    emp.salary = new_salary

    emp.display()