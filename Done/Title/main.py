# Title: Titles.txt
# In-class exercise
# Starting Out With Python, 5th Edition
# Date: 2/14/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith


def main():

    # Open file
    infile = open(r'titles.txt','r')

    # Read file contents to var
    file_contents = infile.read()

    # Close file
    infile.close()

    # Print records
    print(file_contents)


# Call the main func
if __name__ == '__main__':
    main()
