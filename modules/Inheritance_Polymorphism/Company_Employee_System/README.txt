How super() Works in This Project
(a) Calling Parent Constructor
super().__init__(name)

This calls the Person constructor from Employee.

(b) Extending Parent Method
super().show_details()

This first prints Person details, then adds Employee details.

(c) Diamond Problem Resolution

Structure:

        Person
           |
        Employee
        /      \
 Department    |
        \      /
          Manager

When super() is used, Python follows MRO:

Manager → Employee → Person → Department → object

This prevents calling the same parent multiple tim