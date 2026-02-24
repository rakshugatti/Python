# Program to check if the birth year is a leap year
# and display the day of the week for the given date of birth
# Author: Your Name
# Description: Uses datetime module for day calculation

from datetime import datetime

# Taking date of birth input from user
# Expected format: DD-MM-YYYY
dob_input = input("Enter your Date of Birth (DD-MM-YYYY): ")

# Convert string input into datetime object
dob = datetime.strptime(dob_input, "%d-%m-%Y")

# Extract year from the given date
year = dob.year

# Determine if the year is a leap year
if year % 400 == 0:
    leap_status = "Leap Year"
elif year % 100 == 0:
    leap_status = "Not a Leap Year"
elif year % 4 == 0:
    leap_status = "Leap Year"
else:
    leap_status = "Not a Leap Year"

# Get the day of the week
day_of_week = dob.strftime("%A")

# Display results
print("\n----- Result -----")
print(f"Date of Birth : {dob_input}")
print(f"Day           : {day_of_week}")
print(f"Year {year} is a {leap_status}.")