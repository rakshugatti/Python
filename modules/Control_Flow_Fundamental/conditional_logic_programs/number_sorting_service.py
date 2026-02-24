# Program to arrange three numbers in ascending order
# Author: Your Name
# Description: Sorts three numbers manually using conditional statements

# Taking input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Compare numbers to determine smallest, middle, and largest
if num1 <= num2 and num1 <= num3:
    smallest = num1
    
    if num2 <= num3:
        middle = num2
        largest = num3
    else:
        middle = num3
        largest = num2

elif num2 <= num1 and num2 <= num3:
    smallest = num2
    
    if num1 <= num3:
        middle = num1
        largest = num3
    else:
        middle = num3
        largest = num1

else:
    smallest = num3
    
    if num1 <= num2:
        middle = num1
        largest = num2
    else:
        middle = num2
        largest = num1

# Displaying the result
print("Numbers in ascending order:", smallest, middle, largest)# Program to arrange three numbers in ascending order
# Description: Sorts three numbers manually using conditional statements

# Taking input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Compare numbers to determine smallest, middle, and largest
if num1 <= num2 and num1 <= num3:
    smallest = num1
    
    if num2 <= num3:
        middle = num2
        largest = num3
    else:
        middle = num3
        largest = num2

elif num2 <= num1 and num2 <= num3:
    smallest = num2
    
    if num1 <= num3:
        middle = num1
        largest = num3
    else:
        middle = num3
        largest = num1

else:
    smallest = num3
    
    if num1 <= num2:
        middle = num1
        largest = num2
    else:
        middle = num2
        largest = num1

# Displaying the result
print("Numbers in ascending order:", smallest, middle, largest)