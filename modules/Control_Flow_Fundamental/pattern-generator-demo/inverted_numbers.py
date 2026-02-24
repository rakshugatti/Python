"""
Description: Prints an inverted number triangle using nested loops.
"""

def inverted_triangle(rows: int) -> None:
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

if __name__ == "__main__":
    inverted_triangle(5)