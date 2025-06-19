# Title: Updating List (Friends)
# In-class exercise
# Starting Out With Python, 5th Edition
# Date: 2/21/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Create list
    friends = ['Amy', 'Bob', 'Carol', 'Dave', 'Eva']

    # Read, update & read
    print_list()
    friends[2] = 'John'
    friends[4] = 'Billy'
    print()
    print_list()


def print_list(list_name):
    index = 0
    while index < len(list_name):
        print(list_name[index])
        index += 1


# Call the main function.
if __name__ == '__main__':
    main()