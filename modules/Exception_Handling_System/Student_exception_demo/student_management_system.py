import math

print("\n--- Student Management System ---\n")

# 1. ValueError
try:
    age = int("abc")
except ValueError:
    print("ValueError: Invalid age input")

# 2. IndexError
try:
    subjects = ["Math", "Science"]
    print(subjects[5])
except IndexError:
    print("IndexError: Subject not found")

# 3. KeyError
try:
    student = {"name": "John"}
    print(student["age"])
except KeyError:
    print("KeyError: Missing student data")

# 4. TypeError
try:
    result = "Marks: " + 100
except TypeError:
    print("TypeError: Cannot combine string and integer")

# 5. ZeroDivisionError
try:
    total_marks = 500
    num_subjects = 0   # renamed variable (better clarity)
    print(total_marks / num_subjects)
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero")

# 6. FileNotFoundError
try:
    open("students.txt", "r")   # explicitly added mode
except FileNotFoundError:
    print("FileNotFoundError: File not found")

# 7. ModuleNotFoundError
try:
    import xyzmodule
except ModuleNotFoundError:
    print("ModuleNotFoundError: Module not installed")

# 8. AttributeError
try:
    num = 10
    num.append(5)
except AttributeError:
    print("AttributeError: Invalid method for object")

# 9. RuntimeError
try:
    raise RuntimeError("Manual error")
except RuntimeError:
    print("RuntimeError: System error occurred")

# 10. OverflowError
try:
    print(math.exp(1000))
except OverflowError:
    print("OverflowError: Number too large")

print("\nSystem execution completed")