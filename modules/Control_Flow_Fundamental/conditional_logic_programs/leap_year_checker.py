# Program to check whether a given year is a leap year
# Author: Your Name
# Description: Determines if a year is a leap year based on standard rules

# Take year input from user
year = int(input("Enter a year: "))

# Leap year logic:
# 1. If year is divisible by 400 → Leap Year
# 2. Else if year is divisible by 100 → Not a Leap Year
# 3. Else if year is divisible by 4 → Leap Year
# 4. Otherwise → Not a Leap Year

if year % 400 == 0:
    print(f"{year} is a Leap Year.")
elif year % 100 == 0:
    print(f"{year} is Not a Leap Year.")
elif year % 4 == 0:
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is Not a Leap Year.")