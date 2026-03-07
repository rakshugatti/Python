# File: stack_balanced_parentheses_trial.py

# Stack class
class Stack:

    def __init__(self):
        self.items = []

    # Push operation
    def push(self, value):
        self.items.append(value)
        print("Push:", value)
        print("Stack:", self.items)

    # Pop operation
    def pop(self):
        if len(self.items) == 0:
            print("Stack is Empty")
        else:
            removed = self.items.pop()
            print("Pop:", removed)
            print("Stack:", self.items)

    # Peek operation
    def peek(self):
        if len(self.items) == 0:
            print("Stack is Empty")
        else:
            print("Top element:", self.items[-1])

    # Check empty
    def isEmpty(self):
        if len(self.items) == 0:
            print("Stack is Empty")
        else:
            print("Stack is Not Empty")

    # Size
    def size(self):
        print("Stack Size:", len(self.items))

    # Display stack
    def display(self):
        print("Current Stack:", self.items)


# Create stack object
stack = Stack()

while True:

    print("\n---- STACK MENU ----")
    print("1 Push Bracket")
    print("2 Pop Bracket")
    print("3 Peek")
    print("4 Check Empty")
    print("5 Size")
    print("6 Check Balanced Parentheses")
    print("7 Display Stack")
    print("8 Exit")

    choice = int(input("Enter choice: "))

    # Push
    if choice == 1:
        value = input("Enter bracket ( ( { [ ): ")
        stack.push(value)

    # Pop
    elif choice == 2:
        stack.pop()

    # Peek
    elif choice == 3:
        stack.peek()

    # isEmpty
    elif choice == 4:
        stack.isEmpty()

    # Size
    elif choice == 5:
        stack.size()

    # Check balanced expression
    elif choice == 6:

        expression = input("Enter expression: ")

        temp_stack = Stack()

        pairs = {')':'(', '}':'{', ']':'['}

        balanced = True

        for char in expression:

            if char in "({[":
                temp_stack.push(char)

            elif char in ")}]":

                if len(temp_stack.items) == 0:
                    balanced = False
                    break

                top = temp_stack.items.pop()

                if pairs[char] != top:
                    balanced = False
                    break

        if len(temp_stack.items) != 0:
            balanced = False

        if balanced:
            print("Expression is Balanced")
        else:
            print("Expression is Not Balanced")

    # Display
    elif choice == 7:
        stack.display()

    # Exit
    elif choice == 8:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")