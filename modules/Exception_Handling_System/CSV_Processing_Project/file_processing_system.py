import csv
import os

# -------------------------------
# Custom Exceptions
# -------------------------------
class ValidationError(Exception):
    pass

class InvalidIDError(ValidationError):
    pass

class InvalidNameError(ValidationError):
    pass

class InvalidMarksError(ValidationError):
    pass


# -------------------------------
# Validation Function
# -------------------------------
def validate_row(row):
    try:
        student_id = int(row[0])
        name = row[1]
        marks = float(row[2])

        if student_id <= 0:
            raise InvalidIDError("Invalid ID")

        if not name.isalpha():
            raise InvalidNameError("Invalid Name")

        if marks < 0 or marks > 100:
            raise InvalidMarksError("Invalid Marks")

        return True

    except ValueError:
        raise ValidationError("Data type error")


# -------------------------------
# Main Processing Function
# -------------------------------
def process_file():
    valid_count = 0
    invalid_count = 0

    try:
        # ✅ Correct file path handling
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "students.csv")
        error_path = os.path.join(base_path, "error_log.txt")

        with open(file_path, "r") as file:
            reader = csv.reader(file)

            with open(error_path, "w") as error_file:

                for row in reader:
                    try:
                        if validate_row(row):
                            print("✅ Valid Row:", row)
                            valid_count += 1

                    except ValidationError as e:
                        print("❌ Invalid Row:", row, "| Reason:", e)
                        error_file.write(f"{row} -> {e}\n")
                        invalid_count += 1

    except FileNotFoundError:
        print("❌ CSV file not found (Check file location)")

    except PermissionError:
        print("❌ Permission denied")

    except csv.Error:
        print("❌ CSV format error")

    except Exception as e:
        print("❌ Unexpected error:", e)

    finally:
        print("\n--- Summary Report ---")
        print("Total Valid Rows   :", valid_count)
        print("Total Invalid Rows :", invalid_count)


# -------------------------------
# Run Program
# -------------------------------
process_file()