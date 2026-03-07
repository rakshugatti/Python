import copy

# Shopping cart items
cart = ["Laptop", "Mouse", "Keyboard", "Monitor"]

print("Original Cart:", cart)

# 1. append() - Customer adds a new item
cart.append("Headphones")
print("\nAfter adding Headphones:", cart)

# 2. insert() - Priority item added at specific position
cart.insert(1, "USB Cable")
print("After inserting USB Cable at position 1:", cart)

# 3. extend() - Adding multiple items during sale
cart.extend(["Webcam", "Mouse Pad"])
print("After adding sale items:", cart)

# 4. remove() - Customer removes unwanted item
cart.remove("Keyboard")
print("After removing Keyboard:", cart)

# 5. pop() - Remove last added item
removed_item = cart.pop()
print("After pop():", cart)
print("Removed item:", removed_item)

# 6. index() - Find position of an item
print("Index of Monitor:", cart.index("Monitor"))

# 7. count() - Count how many times item appears
cart.append("Mouse")
print("Number of 'Mouse' items:", cart.count("Mouse"))

# 8. sort() - Sort items alphabetically
cart.sort()
print("Sorted Cart:", cart)

# 9. reverse() - Reverse the order
cart.reverse()
print("Reversed Cart:", cart)

# 10. copy() - Create backup of cart
backup_cart = cart.copy()
print("Backup Cart:", backup_cart)

# 11. clear() - Empty cart after checkout
temp_cart = cart.copy()
temp_cart.clear()
print("Cart after checkout:", temp_cart)

print("\n------ Shallow Copy vs Deep Copy Example ------")

# Nested list example: Category with products
store = [
    ["Laptop", "Tablet"],
    ["Mouse", "Keyboard"]
]

# Shallow Copy
shallow_store = copy.copy(store)

# Deep Copy
deep_store = copy.deepcopy(store)

# Modify original store
store[0][0] = "Gaming Laptop"

print("Original Store:", store)
print("Shallow Copy Store:", shallow_store)
print("Deep Copy Store:", deep_store)