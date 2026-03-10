class LinkedList:

    # Inner Node class
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    # Constructor
    def __init__(self):
        self.head = None

    # 1. Append
    def append(self, data):
        new = self.Node(data)

        if not self.head:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new

    # 2. Prepend
    def prepend(self, data):
        new = self.Node(data)
        new.next = self.head
        self.head = new

    # 3. Insert at position
    def insert_at_position(self, data, pos):

        new = self.Node(data)

        if pos == 0:
            self.prepend(data)
            return

        temp = self.head

        for i in range(pos - 1):
            temp = temp.next

        new.next = temp.next
        temp.next = new

    # 4. Delete by value
    def delete_by_value(self, value):

        temp = self.head

        if temp and temp.data == value:
            self.head = temp.next
            return

        while temp.next:

            if temp.next.data == value:
                temp.next = temp.next.next
                return

            temp = temp.next

    # 5. Search
    def search(self, value):

        temp = self.head
        pos = 0

        while temp:

            if temp.data == value:
                return pos

            temp = temp.next
            pos += 1

        return -1

    # 6. Display
    def display(self):

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 7. Reverse
    def reverse(self):

        prev = None
        current = self.head

        while current:

            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        self.head = prev

    # 8. Find length
    def find_length(self):

        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        return count


# -------- Main Program --------

ll = LinkedList()

# Operation 1: Append elements
n = int(input("Enter number of elements to append: "))
for i in range(n):
    value = int(input("Enter value: "))
    ll.append(value)

# Operation 2: Display
print("\nLinked List after append:")
ll.display()

# Operation 3: Prepend
x = int(input("\nEnter value to prepend: "))
ll.prepend(x)

# Operation 4: Display
print("List after prepend:")
ll.display()

# Operation 5: Insert at position
value = int(input("\nEnter value to insert: "))
pos = int(input("Enter position: "))
ll.insert_at_position(value, pos)

# Operation 6: Display
print("List after insertion:")
ll.display()

# Operation 7: Delete
d = int(input("\nEnter value to delete: "))
ll.delete_by_value(d)

# Operation 8: Display
print("List after deletion:")
ll.display()

# Operation 9: Search
s = int(input("\nEnter value to search: "))
position = ll.search(s)

if position != -1:
    print("Element found at position:", position)
else:
    print("Element not found")

# Operation 10: Find length
print("\nLength of Linked List:", ll.find_length())

# Operation 11: Reverse
print("\nReversed Linked List:")
ll.reverse()
ll.display()