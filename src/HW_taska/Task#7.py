# Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.

year = int(input("Enter a year\n"))

if year%4 == 0 and  year%100 != 0:
    print("This is a Leap year")
elif year%400 == 0:
    print("This is a Leap year")
else:
    print("This is not a Leap year")

