# Title: Sentence converter (Upper-Lower)
# In-class Exercise
# Starting Out With Python, 5th Edition
# Date: 2/26/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Get input
    user_input = str(input("Enter a sentence w/o spaces; use uppercase for each new word's first letter: "))

    # Declare vars
    result = ''

    # Insert 1st letter
    result = result + user_input[0]

    for i in range(1, len(user_input)):
        # Get char
        char = user_input[i]

        # Convert uppercase letter to lowercase & insert a space
        if char.isupper():
            char = char.lower()
            result = result + ' '

        # Insert letter
        result = result + char

    # Display results
    print(result)


# Call the main func
if __name__ == '__main__':
    main()
