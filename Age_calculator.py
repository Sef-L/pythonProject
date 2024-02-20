# Create a program that calculates a person's age in years, months, and days.
# Ask the user to enter their birth year, month, and day.
# Calculate and print their age in years, months, and days based on the current date.
import calendar
from _datetime import datetime

now = datetime.now()

input = input("Please enter your birthday in \'MM/DD/YYYY\' format: ")
bday = input.split("/")
if len(bday) != 3:
    print("Please use your brain when providing the date. The input has to be in DD/MM/YYYY.")
    exit()
month, day, year = bday
try:
    month = int(month)
except ValueError:
    print("Please use your brain when providing the date. The month is not a number.")
    exit()
try:
    day = int(day)
except ValueError:
    print("Please use your brain when providing the date. The day is not a number.")
    exit()
try:
    year = int(year)
except ValueError:
    print("Please use your brain when providing the date. The year is not a number.")
    exit()

if month > 12 or month < 1:
    print("Please use your brain when providing the date. The month is not possible.")
    exit()
elif month == 12 and day > 31:
    print("Please use your brain when providing the date. The day is not possible.")
    exit()
elif month == 11 and day > 30:
    print("Please use your brain when providing the date. The day is not possible.")
    exit()
elif month == 10 and day > 31:
    print("Please use your brain when providing the date. The day is not possible.")
    exit()
elif month == 9 and day > 30:
    print("Please use your brain when providing the date. The day is not possible.")
    exit()
elif month == 8 and day > 31:
    print("Please use your brain when providing the date. The day is not possible.")
    exit()
elif month == 7 and day > 31:
    print("Please use your brain when providing the date. The day is not possible.")
    exit()
elif month == 6 and day > 30:
    print("Please use your brain when providing the date. The day is not possible.")
    exit()
elif month == 5 and day > 31:
    print("Please use your brain when providing the date. The day is not possible.")
    exit()
elif month == 4 and day > 30:
    print("Please use your brain when providing the date. The day is not possible.")
    exit()
elif month == 3 and day > 31:
    print("Please use your brain when providing the date. The day is not possible.")
    exit()
elif month == 2 and day > 29 and calendar.isleap(year):
    print("Please use your brain when providing the date. The day is not possible.")
    exit()
elif month == 2 and day > 28 and not calendar.isleap(year):
    print("Please use your brain when providing the date. The day is not possible.")
    exit()
elif month == 1 and day > 31:
    print("Please use your brain when providing the date. The day is not possible.")
    exit()
elif year > now.year or year < 1:
    print("Please use your brain when providing the date. The year is not valid.")
    exit()
else:
    birthdate = datetime.strptime(input, "%m/%d/%Y")
    age = now - birthdate
    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30
print(f"You are {years} years, {months} months, and {days} days old!")