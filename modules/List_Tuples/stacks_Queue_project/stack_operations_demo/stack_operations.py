# File: stack_operations.py

# Stack class using Python list
class Stack:

    # Constructor
    def __init__(self):
        self.items = []

    # Push operation (insert element)
    def push(self, value):
        self.items.append(value)
        print(value, "pushed into stack")

    # Pop operation (remove top element)
    def pop(self):
        if not self.isEmpty():
            removed = self.items.pop()
            print("Popped element:", removed)
        else:
            print("Stack is empty. Cannot pop.")

    # Peek operation (view top element)
    def peek(self):
        if not self.isEmpty():
            print("Top element is:", self.items[-1])
        else:
            print("Stack is empty.")

    # Check if stack empty
    def isEmpty(self):
        return len(self.items) == 0

    # Return stack size
    def size(self):
        print("Stack size:", len(self.items))

    # Display stack
    def display(self):
        print("Current Stack:", self.items)


# Create stack object
stack = Stack()

# Number of inputs
n = int(input("Enter number of values to push: "))

# Push n numbers
for i in range(n):
    num = int(input("Enter number: "))
    stack.push(num)

print()

# Trial and error menu using if conditions
while True:

    print("\n--- Stack Operations Menu ---")
    print("1 Push")
    print("2 Pop")
    print("3 Peek")
    print("4 Check Empty")
    print("5 Size")
    print("6 Display")
    print("7 Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to push: "))
        stack.push(value)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.peek()

    elif choice == 4:
        if stack.isEmpty():
            print("Stack is Empty")
        else:
            print("Stack is Not Empty")

    elif choice == 5:
        stack.size()

    elif choice == 6:
        stack.display()

    elif choice == 7:
        print("Program Ended")
        break

    else:
        print("Invalid choice")