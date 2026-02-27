from array import array


def main():

    # Step 1: Create integer array
    numbers = array('i', [10, 20, 30, 40, 50])
    print("Initial Array:", numbers)

    # Step 2: Insertion
    numbers.insert(2, 25)  # Insert 25 at index 2
    print("After Insertion:", numbers)

    # Step 3: Deletion
    numbers.remove(40)  # Remove element 40
    print("After Deletion:", numbers)

    # Step 4: Traversal
    print("Traversing Array:")
    for num in numbers:
        print(num, end=" ")
    print()

    # Step 5: Searching (Linear Search)
    key = 30
    found = False

    for i in range(len(numbers)):
        if numbers[i] == key:
            print(f"Element {key} found at index {i}")
            found = True
            break

    if not found:
        print("Element not found")


if __name__ == "__main__":
    main()