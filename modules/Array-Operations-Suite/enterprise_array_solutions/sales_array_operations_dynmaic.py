"""
Enterprise Sales Analytics System (Dynamic Version)

Description:
- Accepts n inputs (numbers or strings)
- Performs:
  1. Linear Search
  2. Binary Search
  3. Rotation
  4. Second Highest (numbers only)
  5. Remove Duplicates
"""


# ---------------------------------------------------------
# Linear Search
# ---------------------------------------------------------
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


# ---------------------------------------------------------
# Binary Search (Sorted Required)
# ---------------------------------------------------------
def binary_search(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ---------------------------------------------------------
# Rotate Array
# ---------------------------------------------------------
def rotate_array(data, k):
    n = len(data)
    k = k % n

    rotated = [0] * n

    for i in range(n):
        new_index = (i + k) % n
        rotated[new_index] = data[i]

    return rotated


# ---------------------------------------------------------
# Second Highest (Only for Numbers)
# ---------------------------------------------------------
def second_highest(data):
    largest = float('-inf')
    second = float('-inf')

    for value in data:
        if value > largest:
            second = largest
            largest = value
        elif value > second and value != largest:
            second = value

    if second == float('-inf'):
        return None
    return second


# ---------------------------------------------------------
# Remove Duplicates
# ---------------------------------------------------------
def remove_duplicates(data):
    unique_data = []

    for value in data:
        exists = False
        for item in unique_data:
            if item == value:
                exists = True
                break

        if not exists:
            unique_data.append(value)

    return unique_data


# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------
def main():

    n = int(input("Enter number of elements: "))

    data = []

    print("Enter elements (numbers or strings):")

    for i in range(n):
        value = input(f"Element {i+1}: ")

        # Try converting to integer if possible
        if value.isdigit():
            data.append(int(value))
        else:
            data.append(value)

    print("\nOriginal Data:", data)

    # Linear Search
    target = input("\nEnter value to search: ")

    if target.isdigit():
        target = int(target)

    print("Linear Search Index:", linear_search(data, target))

    # Binary Search (need sorted copy)
    sorted_data = sorted(data)
    print("\nSorted Data for Binary Search:", sorted_data)
    print("Binary Search Index:", binary_search(sorted_data, target))

    # Rotate
    k = int(input("\nEnter rotation value (k): "))
    print("Rotated Data:", rotate_array(data, k))

    # Second Highest (only if numbers)
    if all(isinstance(x, int) for x in data):
        print("Second Highest:", second_highest(data))
    else:
        print("Second Highest not applicable for strings.")

    # Remove Duplicates
    print("After Removing Duplicates:", remove_duplicates(data))


if __name__ == "__main__":
    main()