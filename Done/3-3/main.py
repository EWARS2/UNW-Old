# Title: Age Classifier
# Chapter 3, Exercise 3
# Starting Out With Python, 5th Edition
# Date: 2/7/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

# Define constants
THRESHOLD_INFANT   = 1
THRESHOLD_CHILD    = 13
THRESHOLD_TEENAGER = 20

# Get age from user
age = int(round(float(input("Input age in years: "))))

# Classify & Disp name
if age <= THRESHOLD_INFANT:

    print ("Age: Infant")

elif age < THRESHOLD_CHILD:

    print ("Age: Child")

elif age < THRESHOLD_TEENAGER:

    print ("Age: Teenager")

else:

    print ("Age: Adult")


