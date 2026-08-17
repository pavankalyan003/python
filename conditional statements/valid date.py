 #Write a program that accepts a year, month, and day, and determines whether the date is
#valid, accounting for leap years and the number of days in each month.
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
day = int(input("Enter day: "))

# Determine the number of days in the month
if month == 2:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        max_days = 29
    else:
        max_days = 28
elif month in [4, 6, 9, 11]:
    max_days = 30
elif 1 <= month <= 12:
    max_days = 31
else:
    max_days = 0

# Check whether the date is valid
if year > 0 and 1 <= month <= 12 and 1 <= day <= max_days:
    print("Valid date")
else:
    print("Invalid date")
