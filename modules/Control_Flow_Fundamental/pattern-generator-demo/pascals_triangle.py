"""
 Prints first 5 rows of Pascal's Triangle.
"""

def pascals(rows: int) -> None:
    for i in range(rows):
        number = 1
        for j in range(rows - i):
            print(" ", end=" ")
        for j in range(i + 1):
            print(number, end=" ")
            number = number * (i - j) // (j + 1)
        print()

if __name__ == "__main__":
    pascals(5)