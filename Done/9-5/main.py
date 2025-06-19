# Title: Word Frequency
# Chapter 9, Exercise 5
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Get input
    my_dictionary = txt2dict(read(str(input("Enter the path/name of a raw text file to process: "))))

    # Fancy output
    print()
    print("Count  Word")
    print("===========")
    for x, y in my_dictionary.items():
        print(f'{y:<5.0f}x {x.capitalize()}')


def read(file_name):
    # Convert filename to string
    file_name = str(file_name)

    try:
        # Open file
        file_variable = open(file_name, 'r')

        # Read contents
        file_contents = file_variable.read()

        # Close the file
        file_variable.close()

    except FileNotFoundError:
        # Set a default message if nothing is found.
        file_contents = "The file wasn't found."

    # Return the contents of the file
    return file_contents


def txt2dict(txt_input):
    # Cleanup text for easier processing
    txt_input = txt_input.upper()
    txt_input = txt_input.replace("\n", " ")
    txt_input = txt_input.replace(".", "")

    # Convert string to list to tuple
    txt_input = tuple(txt_input.split(' '))

    # Create a blank dictionary
    txt_output = {}

    # Process into dictionary
    for x in txt_input:
        if x in txt_output:
            txt_output[x] += 1
        else:
            txt_output[x] = 1

    # Remove entries for double-spaces,
    # Which are usually created by the earlier cleanup.
    txt_output.pop("")

    # Return finalized result
    return txt_output


# Call the main func
if __name__ == '__main__':
    main()