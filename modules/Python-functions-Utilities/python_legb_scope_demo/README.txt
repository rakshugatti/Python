Python Scope and the LEGB Rule (with a Real-Time Example)

In Python, scope refers to the region of a program where a variable can be accessed or modified. Python resolves variable names using the LEGB rule, which defines the order in which Python searches for variables.

LEGB stands for:

L – Local

E – Enclosing

G – Global

B – Built-in

Python checks these scopes in this exact order.

1. Local Scope (L)

The local scope contains variables defined inside a function.

Accessible only within that function.

Created when the function is called.

Example:

def calculate_total():
    price = 100   # Local variable
    print("Price:", price)

calculate_total()

Here, price exists only inside calculate_total().

2. Enclosing Scope (E)

The enclosing scope appears in nested functions.
It refers to variables in the outer function.

Example:

def outer():
    discount = 10   # Enclosing variable

    def inner():
        print("Discount:", discount)

    inner()

outer()

inner() can access discount from outer().

3. Global Scope (G)

Variables defined outside all functions are global.

Accessible throughout the program.

To modify them inside a function, we use the global keyword.

Example:

tax = 5

def show_tax():
    print("Tax:", tax)

show_tax()
4. Built-in Scope (B)

This contains Python’s predefined functions and names, such as:

print()

len()

sum()

Example:

numbers = [1, 2, 3]
print(len(numbers))

Python finds len() in the built-in scope.
-------------------------------------------------------------------------------------------------------------------------
Key Concepts Demonstrated
Variable Shadowing

A variable in a smaller scope hides a variable with the same name in a larger scope.

Example:

global x → enclosing x → local x

The closest scope wins.

global Keyword

Allows a function to modify a global variable.

global x

Without global, Python would create a new local variable.

nonlocal Keyword

Used in nested functions to modify a variable in the enclosing scope.

nonlocal y

It does not refer to global scope, only the nearest enclosing function.

✅ Summary

Search order for variables:

Local → Enclosing → Global → Built-in

Local: Inside current function

Enclosing: Outer function in nested functions

Global: Module level

Built-in: Python predefined names

If you'd like, I can also show a visual diagram of LEGB lookup or tricky interview examples where scope causes bugs.