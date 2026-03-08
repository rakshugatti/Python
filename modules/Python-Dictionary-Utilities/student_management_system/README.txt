Nested Dictionaries in Python

A nested dictionary is a dictionary inside another dictionary.
It is useful when we want to store structured or hierarchical data.

Syntax Example

students = {
    "Alice": {"Math": 85, "Science": 90},
    "Bob": {"Math": 78, "Science": 88}
}

Here:

Outer dictionary key → Student Name

Inner dictionary → Subjects and Marks

So the structure becomes:

student_name → {subject → marks}

Example access:

print(students["Alice"]["Math"])  # Output: 85