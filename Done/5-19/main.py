# Title: Future Value
# Chapter 5, Exercise 19
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Get input from user
    inPresent  = float(input("Enter the account's present value: $"))
    inInterest = float(input("Enter the account's monthly interest rate: %"))
    inTime     = float(input("Enter the number of months passed: "))

    # CALCULATE THE FUTURE!!! (Future value, that is.)
    outFutureVal = future_value(inPresent, inInterest, inTime)
    
    # Display results
    print(f'\nAfter this time, the account will hold ${outFutureVal:,.2f}')


def future_value(present_value, interest_rate, time_months):
    # Convert interest rate into a proper percentage
    interest_rate /= 100
    
    # Calculate & return the Future Value
    return present_value * (( 1 + interest_rate ) ** time_months)


# Call the main func
if __name__ == '__main__':
    main()
