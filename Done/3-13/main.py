# Title: Shipping Charges
# Chapter 3, Exercise 13
# Starting Out With Python, 5th Edition
# Date: 2/7/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

print ("Fast Freight Shipping Company\n")

# Declare constants
WEIGHT_A = 2
WEIGHT_B = 6
WEIGHT_C = 10

# Rates are in USD currency
RATE_A = 1.50
RATE_B = 3.00
RATE_C = 4.00
RATE_D = 4.75

# Get weight from user
weight = float(input("How much does your package weigh in pounds? :"))

# Determine rate
if weight <= WEIGHT_A:
    rate = RATE_A
elif weight <= WEIGHT_B:
    rate = RATE_B
elif weight <= WEIGHT_C:
    rate = RATE_C
else:
    rate = RATE_D

# Display results
print (f"Shipping charges: ${rate:,.2f}")

