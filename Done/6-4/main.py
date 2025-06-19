# Title: Item Counter
# Chapter 6, Exercise 4
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Open names.txt for reading
    file_variable = open('names.txt','r')

    # Declare vars
    counter = 0

    # For every line
    while 1:
        # Get line & clear formatting
        line = file_variable.readline()
        line = line.rstrip()

        # If end of file, break.
        if line=='':
            break
        else:
            # Inc counter
            counter+=1
            
            # Display current line
            print(f'{counter:>3} {line}')

    # Display result
    print(f'\nEntry count: {counter}')
    print('Do note that this program treats blank lines as end of file.')


# Call the main func
if __name__ == '__main__':
    main()
