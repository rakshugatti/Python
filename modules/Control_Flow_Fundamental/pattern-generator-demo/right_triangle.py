"""

Description: Prints a right-angled triangle pattern using nested loops.
"""

def right_triangle(rows: int) -> None:
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    right_triangle(5)