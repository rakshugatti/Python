def diamond(rows: int) -> None:

    # Upper half
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print("*", end=" ")
        print()

    # Lower half
    for i in range(rows - 1, 0, -1):
        for j in range(rows - i):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    diamond(4)