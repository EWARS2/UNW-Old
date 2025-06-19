# Title: 
# Chapter 2, Exercise 9
# Starting Out With Python, 5th Edition
# Date: 2/7/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

# Obtain information and convert it accordingly
principle = float(input(
    "Input principle (original deposit): $"))

rateInterestAnnual = float(input(
    "Input annual interest rate: %"))/100

nPerYr = float(input(
    "How many times per year interest is compounded: "))

timeYrs = float(input(
    "Input how many years: "))



# Calculate amount
account = principle * (
    ( 1 + ( rateInterestAnnual / nPerYr ) )
    ** ( nPerYr * timeYrs ) )

# Disp output
print (f"Final balance: ${account:,.2f}")

