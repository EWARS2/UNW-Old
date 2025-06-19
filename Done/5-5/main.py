# Title: Property Tax
# Chapter 5, Exercise 5
# Starting Out With Python, 5th Edition
# Date: 2/7/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Get input
    inActualVal = float(input("Enter the actual property value: $"))

    # Assessment Value is used multiple times, so calculate it
    assessmentValue = assessment_value(inActualVal)

    # Disp results w/ formatting
    print(f'Assessment Value: ${assessmentValue:,.2f}')
    print(f'Property Tax: ${property_tax(assessmentValue):,.2f}')


def assessment_value(actualVal):
    # Define Constants
    VALUE_RATE = .60 # Percentage

    # Return calculated result
    return ( VALUE_RATE * actualVal )

def property_tax(assessmentVal):
    # Define Constants
    TAX_RATE = 0.0072 # $0.72 / $100.00

    # Return calculated result
    return ( TAX_RATE * assessmentVal )


# Call the main func
if __name__ == '__main__':
    main()
