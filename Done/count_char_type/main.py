# Title: count_char_type
# In-class Exercise
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Get text
    text = read('text.txt')

    # Dec vars
    count_upper = count_lower = count_digit = count_space = count_other = 0

    # Count characters!
    for char in text:
        if char.isupper():
            count_upper +=1
        elif char.islower():
            count_lower += 1
        elif char.isdigit():
            count_digit += 1
        elif char.isspace():
            count_space += 1
        else:
            count_other += 1

    # Disp results
    print(f'Uppercase count: {count_upper}')
    print(f'Lowercase count: {count_lower}')
    print(f'Digit count: {count_digit}')
    print(f'Space count: {count_space}')
    print(f'Other characters: {count_other}')


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


# Call the main func
if __name__ == '__main__':
    main()