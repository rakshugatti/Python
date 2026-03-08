Difference Between Class Variables and Instance Variables
Class Variable
A class variable is a variable that is shared by all objects of a class. It is defined inside the class but outside any method.

Key points:

Same value for all objects
Stored only once in memory
Accessed using the class name or object name

Instance Variable
An instance variable is a variable that is unique to each object. It is defined inside the constructor (__init__) using self.

Key points:

Each object has its own copy
Value can be different for different objects
Accessed using the object name.

Explanation

school_name is a class variable, so when it is changed using Student.school_name, the change affects all objects.

name, roll_no, and marks are instance variables, so they remain different for each student object.