"""
Main module - Handles user interaction.
"""

from models import Student


def collect_marks() -> list[float]:
    print("Enter marks for five subjects:")
    return [float(input(f"Subject {i + 1}: ")) for i in range(5)]


def main() -> None:
    students = []

    print("\n===== MULTI STUDENT RESULT SYSTEM =====")

    while True:
        print("\nEnter Student Details")
        name = input("Name: ").strip()
        roll_number = input("Roll Number: ").strip()
        marks = collect_marks()

        student = Student(name=name, roll_number=roll_number, marks=marks)
        students.append(student)

        choice = input("\nAdd another student? (y/n): ").lower()
        if choice != "y":
            break

    print("\n\n========= FINAL RESULTS =========")

    for student in students:
        print(student.generate_report())


if __name__ == "__main__":
    main()