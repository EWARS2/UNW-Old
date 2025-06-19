# Title: Employee ID
# In-Class Exercise
# Starting Out With Python, 5th Edition
# Date: 2/7/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

count = 0


def main():
    first = str(input("First name: "))
    last = str(input("Last name: "))
    employee(first, last)


def employee(str1, str2):
    global count
    count += 1
    full = str1 + ' ' + str2
    print(f'Full name: {full}')
    print(f'Employee ID: {count}')
    return


# Call the main func
if __name__ == '__main__':
    main()
