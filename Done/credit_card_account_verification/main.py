# Title: Credit Card Account Verification
# Mid-term Challenge
# Starting Out With Python, 5th Edition
# Date: 3/4/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Get numbers
    numbers = txt2tuple(read('credit_card.txt'))

    while 1:
        # Get input
        while 1:
            try:
                in_name = float(input('(Type q to quit.) Enter a number to search for: '))
                break
            except ValueError:
                print("Error: Input is not a number, please try again.\n")

        # Q to quit
        if in_name == 'Q' or in_name == 'q':
            break

        # Check lists & display results
        if in_name in numbers:
            print(f'{in_name} is in our list of credit card numbers.')
        else:
            print(f'{in_name} is not within our list of credit card numbers.')


def read(file_name):
    # Convert filename to string
    file_name = str(file_name)

    # Open file
    file_variable = open(file_name, 'r')

    # Read contents
    file_contents = file_variable.read()

    # Close the file
    file_variable.close()

    # Return the contents of the file
    return file_contents


def txt2tuple(txt_contents):
    # Convert string to list to tuple
    txt_contents = tuple(txt_contents.split('\n'))

    # Return finalized tuple
    return txt_contents


# Call the main func
if __name__ == '__main__':
    main()