# Global variable
tax_rate = 5

def shopping_cart():
    discount = 10   # Enclosing variable

    def add_item():
        price = 100  # Local variable
        tax_rate = 8  # Variable shadowing (local hides global)

        print("Item price:", price)
        print("Local tax rate (shadowing global):", tax_rate)
        print("Discount from enclosing scope:", discount)

    def update_discount():
        nonlocal discount
        discount = 20
        print("Updated discount using nonlocal:", discount)

    add_item()
    update_discount()
    print("Discount after update:", discount)

def update_tax():
    global tax_rate
    tax_rate = 12
    print("Global tax rate updated:", tax_rate)

# Program execution
print("Initial global tax:", tax_rate)

shopping_cart()

update_tax()

print("Final global tax:", tax_rate)

# Built-in scope example
items = ["Laptop", "Mouse", "Keyboard"]
print("Number of items in cart:", len(items))