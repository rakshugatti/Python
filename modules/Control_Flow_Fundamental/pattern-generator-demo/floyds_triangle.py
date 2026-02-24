"""
 Prints Floyd's triangle using nested loops.
"""

def floyds(rows: int) -> None:
    num = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

if __name__ == "__main__":
    floyds(5)
