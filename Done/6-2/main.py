# Title: File Head Display
# Chapter 6, Exercise 2
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    in_name = input("Open filename: ")

    read_file(in_name)

def read_file(file_name):
    # Convert file name to string
    file_name = str(file_name)

    # Open the file for reading
    file_variable = open(file_name,'r')

    # Read the first 5 lines of the file
    line1 = file_variable.readline()
    line2 = file_variable.readline()
    line3 = file_variable.readline()
    line4 = file_variable.readline()
    line5 = file_variable.readline()

    # Close the file
    file_variable.close()

    # Display result
    print(f'{line1}',end='')
    print(f'{line2}',end='')
    print(f'{line3}',end='')
    print(f'{line4}',end='')
    print(f'{line5}',end='')     


# Call the main func
if __name__ == '__main__':
    main()

