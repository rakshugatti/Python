# Single Inheritance
# Company->Developer

class Employee:

    def __init__(self, name):
        self.name = name

    def work(self):
        print(self.name, "works in the company")


class Developer(Employee):

    def code(self):
        print(self.name, "writes Python code")


# Object creation
d = Developer("Rahul")

d.work()
d.code()