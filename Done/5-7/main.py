# Title: Stadium Seating
# Chapter 5, Exercise 7
# Starting Out With Python, 5th Edition
# Date: 2/7/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Get input from user
    inClassA = int(round(float(input(
        "How many tickets sold in Class A? :"))))
    
    inClassB = int(round(float(input(
        "How many tickets sold in Class B? :"))))

    inClassC = int(round(float(input(
        "How many tickets sold in Class C? :"))))

    # Calculate total income
    seatingIncome = seating(inClassA, inClassB, inClassC)

    # Display results
    print(f"Total Income: ${seatingIncome:,.2f}")


def seating(classA,classB,classC):
    # Declare constants
    COST_CLASS_A = 20.00 # $USD
    COST_CLASS_B = 15.00 # $USD
    COST_CLASS_C = 10.00 # $USD

    # Calculate total
    result = ( ( COST_CLASS_A * classA ) +
               ( COST_CLASS_B * classB ) +
               ( COST_CLASS_C * classC ) )

    # Return result
    return result

# Call the main func
if __name__ == '__main__':
    main()

