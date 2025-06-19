# Title: Courses - Prelim
# In-class exercise
# Starting Out With Python, 5th Edition
# Date: 2/21/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith


def main():
    # Create list
    courses = ['COS2005',
               'NAN101',
               'NAN418',
               'NAN404',
               'NAN420',
               'NAN69',
               'MAT9',
               'MAT10',
               'MAT21',
               'COS777'
               ]

    # Get input
    prompt = str(input('Enter a Course ID (Case sensitive): '))

    # Display results
    if prompt in courses:
        print(f'\n{prompt} is present on the list.')
    else:
        print(f'\n{prompt} is NOT present on the list.')


# Call the main function.
if __name__ == '__main__':
    main()