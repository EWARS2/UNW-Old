# Title: Celsius to Fahrenheit Temperature Converter
# Chapter 2, Exercise 9
# Starting Out With Python, 5th Edition
# Date: 2/7/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

# Get temperature from user
tempC = float(input("Temperature in Celsius: "))

# Calculate temperature in Fahrenheit
tempF = ((9/5) * tempC) + 32

# Display results with formatting
print (f"Converted to Fahrenheit: {tempF:,.0f}")

