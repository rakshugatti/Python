from collections import defaultdict

# Example 1: Group Students by Department
def group_students():
    students = [
        ("Alice", "CS"),
        ("Bob", "IT"),
        ("Charlie", "CS"),
        ("David", "IT")
    ]

    dept = defaultdict(list)

    for name, department in students:
        dept[department].append(name)

    print("\nStudents by Department:")
    print(dict(dept))


# Example 2: Word Frequency Counter
def word_count():
    sentence = "python is simple and python is powerful"

    words = defaultdict(int)

    for word in sentence.split():
        words[word] += 1

    print("\nWord Count:")
    print(dict(words))