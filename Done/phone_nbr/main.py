# Title: phone_nbr
# In-class Exercise
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # List comprehension to populate digit_list with digits from 2 to 9
    digit_list = [i for i in range(2, 10)]

    # Get phone number in words from user
    number = input('Enter a phone number in words: ').upper()

    # Initialize new_number variable as null to hold new number
    new_number = ''

    # Loop through every character in the number variable
    for char in number:
        # Initialize empty index variable
        index = None
        if char.isalpha():
            # If char is a letter, assign appropriate index from digit_list
            if char == 'A' or char == 'B' or char == 'C':
                index = 0
            elif char == 'D' or char == 'E' or char == 'F':
                index = 1
            elif char == 'G' or char == 'H' or char == 'I':
                index = 2
            elif char == 'J' or char == 'K' or char == 'L':
                index = 3
            elif char == 'M' or char == 'N' or char == 'O':
                index = 4
            elif char == 'P' or char == 'Q' or char == 'R' or char == 'S':
                index = 5
            elif char == 'T' or char == 'U' or char == 'V':
                index = 6
            elif char == 'W' or char == 'X' or char == 'Y' or char == 'Z':
                index = 7

            # Concatenate digit at specified digit in digit_list
            new_number += str(digit_list[index])

        else:
            # New number is not a digit, just concatenate
            new_number += char

    # Print new number
    print(new_number)


# Call the main func
if __name__ == '__main__':
    main()
