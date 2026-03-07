# File: queue_operations.py

# Queue class using Python list
class Queue:

    # Constructor
    def __init__(self):
        self.items = []

    # Enqueue operation (insert element)
    def enqueue(self, value):
        self.items.append(value)
        print(value, "added to queue")

    # Dequeue operation (remove front element)
    def dequeue(self):
        if not self.isEmpty():
            removed = self.items.pop(0)
            print("Removed element:", removed)
        else:
            print("Queue is empty. Cannot dequeue.")

    # Peek operation (view front element)
    def peek(self):
        if not self.isEmpty():
            print("Front element:", self.items[0])
        else:
            print("Queue is empty")

    # Check if queue is empty
    def isEmpty(self):
        return len(self.items) == 0

    # Queue size
    def size(self):
        print("Queue size:", len(self.items))

    # Display queue
    def display(self):
        print("Current Queue:", self.items)


# Create queue object
queue = Queue()

# Number of inputs
n = int(input("Enter number of values to enqueue: "))

# Add n numbers
for i in range(n):
    num = int(input("Enter number: "))
    queue.enqueue(num)

print()

# Menu driven trial-and-error operations
while True:

    print("\n--- Queue Operations Menu ---")
    print("1 Enqueue")
    print("2 Dequeue")
    print("3 Peek")
    print("4 Check Empty")
    print("5 Size")
    print("6 Display")
    print("7 Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to enqueue: "))
        queue.enqueue(value)

    elif choice == 2:
        queue.dequeue()

    elif choice == 3:
        queue.peek()

    elif choice == 4:
        if queue.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue is Not Empty")

    elif choice == 5:
        queue.size()

    elif choice == 6:
        queue.display()

    elif choice == 7:
        print("Program Ended")
        break

    else:
        print("Invalid choice")