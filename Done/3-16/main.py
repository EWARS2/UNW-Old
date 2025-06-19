# Title: February Days
# Chapter 3, Exercise 16
# Starting Out With Python, 5th Edition
# Date: 2/7/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

# Get year # from user
year = int(round(float(input("Enter a year: "))))

# Check if it's a leap year
# & Store result
if ( year % 100) == 0:
    if ( year % 400) == 0:
        isLeapYear = True
    else:
        isLeapYear = False
elif ( year % 4) == 0:
    isLeapYear = True
else:
    isLeapYear = False


# Code revised for efficiency
# Check if it's a leap year
#if ( year % 4) == 0:
#    isLeapYear = True
#else:
#    isLeapYear = False


# Display result
if isLeapYear:
    print(f"February {year} is a leap year with 29 days.")
else:
    print(f"February {year} isn't a leap year, having only 28 days.")


