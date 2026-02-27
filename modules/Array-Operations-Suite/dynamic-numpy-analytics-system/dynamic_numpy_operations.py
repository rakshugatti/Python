""" Dynamic Enterprise Analytics System

Description:
    - Accepts n numbers from user
    - Creates 1D NumPy array
    - Performs reverse, reshape, transpose
    - Calculates row-wise and column-wise sums
"""

import numpy as np


def main():

    # -----------------------------
    # Step 1: Take dynamic input
    # -----------------------------
    n = int(input("Enter number of elements (n): "))

    elements = []
    print("Enter the elements:")

    for i in range(n):
        value = float(input(f"Element {i + 1}: "))
        elements.append(value)

    # Create 1D NumPy array
    arr_1d = np.array(elements)

    print("\n----- 1D Array -----")
    print("Original Array:", arr_1d)

    # Reverse 1D array
    print("Reversed Array:", arr_1d[::-1])

    # Element-wise operation
    print("Element-wise Multiplication (*2):", arr_1d * 2)

    # -----------------------------
    # Step 2: Convert to 2D (if possible)
    # -----------------------------
    rows = int(input("\nEnter number of rows for 2D reshape: "))
    cols = int(input("Enter number of columns for 2D reshape: "))

    if rows * cols == n:
        arr_2d = arr_1d.reshape(rows, cols)

        print("\n----- 2D Array -----")
        print(arr_2d)

        # Reverse rows
        print("\nReversed 2D (Row-wise):")
        print(arr_2d[::-1])

        # Transpose
        print("\nTransposed Matrix:")
        print(arr_2d.T)

        # Row-wise sum
        print("\nRow-wise Sum:")
        print(arr_2d.sum(axis=1))

        # Column-wise sum
        print("\nColumn-wise Sum:")
        print(arr_2d.sum(axis=0))

    else:
        print("\nReshape not possible (rows × cols must equal n).")


if __name__ == "__main__":
    main()