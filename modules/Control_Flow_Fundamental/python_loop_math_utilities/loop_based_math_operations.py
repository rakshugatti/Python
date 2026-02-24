# Using for loop and range() in all cases


# -------- (a) Multiplication Table --------
number = int(input("Enter a number for multiplication table: "))

print("\nMultiplication Table:")
for i in range(1, 11):   # Using range()
    print(number, "x", i, "=", number * i)


# -------- (b) Factorial --------
num = int(input("\nEnter a number to calculate factorial: "))

factorial = 1
for i in range(1, num + 1):   # Using range()
    factorial = factorial * i

print("Factorial of", num, "is:", factorial)


# -------- (c) Fibonacci Series --------
terms = int(input("\nEnter number of terms for Fibonacci series: "))

first = 0
second = 1

print("Fibonacci Series:")
for i in range(terms):   # Using range()
    print(first, end=" ")
    next_number = first + second
    first = second
    second = next_number