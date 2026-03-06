# (a) Check if a number is prime
def is_prime(n=2):   # default argument
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# (b) GCD using recursion
def gcd(a, b=1):   # default argument
    if b == 0:
        return a
    return gcd(b, a % b)


# (c) Basic calculator
def calculator(a, b, operator='+'):   # default operator
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operator"


# ---------------- MAIN PROGRAM ----------------

# Prime check
num = int(input("Enter a number to check if it is prime: "))
if is_prime(num):        # return value used
    print(num, "is a Prime number")
else:
    print(num, "is NOT a Prime number")


# GCD calculation
a = int(input("\nEnter first number for GCD: "))
b = int(input("Enter second number for GCD: "))
print("GCD of", a, "and", b, "is:", gcd(a, b))


# Calculator
x = float(input("\nEnter first number: "))
y = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

# Using keyword arguments
result = calculator(a=x, b=y, operator=op)
print("Result:", result)