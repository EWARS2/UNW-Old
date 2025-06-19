# Title: Count a # of a specific letter
# In-class Exercise
# Starting Out With Python, 5th Edition
# Date: 2/26/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Declare vars
    count = 0

    # Get input
    name = input ('What is your full name? :')

    # Count the S's
    for char in name:
        if char == 'S' or char =='s':
            count += 1

    # Display results
    if count == 1:
        print(f'1 instance of S in "{name}"')
    else:
        print(f'{count} instances of S in "{name}"')


# Call the main func
if __name__ == '__main__':
    main()
