# Title: Pennies for Pay
# Chapter 4, Exercise 7
# Starting Out With Python, 5th Edition
# Date: 2/7/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():

    # Get # of iterations from user
    in_iterations = int(round(float(input("How many iterations? : "))))

    exponential_growth(in_iterations)


def exponential_growth(iterations):
    # Define Variables
    salary = 0.01
    earnings = 0

    # Display table header
    print("\nDay   Salary   Total Earnings")
    
    for day in range(iterations):
        # Add current salary to current total earnings
        earnings += salary

        # Display current results
        print(f'{(day+1):<6,}${salary:<8,.2f}${earnings:<13,.2f}')

        # Double the salary
        salary *= 2

    # Display final total with formatting
    # Because for loops start at 0, add 1 to the output
    print("\nTotal:")
    print(f'{(day+1):<6,}${salary:<8,.2f}${earnings:<13,.2f}')


# Call the main func
if __name__ == '__main__':
    main()

