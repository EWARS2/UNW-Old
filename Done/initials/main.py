# Title: Initials
# In-class Exercise
# Starting Out With Python, 5th Edition
# Date: 2/26/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Get input
    full_name = str(input("Please input your first, middle & last name: "))

    # Convert to list
    name = full_name.split()

    # Get & Disp initials
    for string in name:
        print(string[0].upper(), sep='', end='. ')



# Call the main func
if __name__ == '__main__':
    main()