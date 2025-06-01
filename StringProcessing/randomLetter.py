# Title: Program #1 -- Random Letters App
# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

import random


def main():
    # Get a string from the user and update it 10x
    my_letters = 'abcdefghijklmnopqrstuvwxyz'
    my_string = input('Enter string to deform :')
    for i in range(10):
        my_string = update(my_string,my_letters)
        print(f'Word #%2d: ' % (i+1) + my_string)


def char_replace(str, pos, char):  # From Moodle
    new_string = str[0:pos] + char + str[pos + 1:]
    return new_string


def update(my_string, replacement_letters=None):
    # Replace characters in a string
    # either with a specific list of characters
    # (If specified)
    # or using characters that are already present
    if replacement_letters is None:
        replacement_letters = my_string
    choice = random.choice(replacement_letters)
    return char_replace(my_string, random.randrange(len(my_string)), choice)


# Call the main func
if __name__ == '__main__':
    main()
