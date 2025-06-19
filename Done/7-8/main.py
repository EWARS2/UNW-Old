# Title: Name Search
# Chapter 7, Exercise 8 
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Get the names into a tuple
    names_boys = txt2tuple(read('BoyNames.txt'))
    names_girls = txt2tuple(read('GirlNames.txt'))

    while 1:
        # Get input
        in_name = str(input('(Type q to quit.) Enter a name to search for: '))

        # Capitalize input to conform to .txt's format
        in_name = in_name.capitalize()

        # Q to quit
        if in_name == 'Q':
            break

        # Check lists & display results
        # This can be cleaned up.
        if in_name in names_boys:
            if in_name in names_girls:
                print(f'{in_name} made the list of most popular Boys AND Girls names! ')
            else:
                print(f'{in_name} made the list of most popular Boys names!')
        elif in_name in names_girls:
            print(f'{in_name} made the list of most popular Girls names!')
        else:
            print(f'{in_name} was not on the list of most popular Boys names.')


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
