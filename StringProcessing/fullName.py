# Title: Program #2 -- Full Name App
# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

def main():
    my_first_name = input("Enter first name :")
    my_middle_name = input("Enter middle name :")
    my_last_name = input("Enter last name :")
    print(fullName(my_first_name, my_middle_name, my_last_name))


def fullName(first_name, middle_name, last_name):
    # Formats name
    return first_name.title() + " " + middle_name.title()[0] + ". " + last_name.title()


# Call the main func
if __name__ == '__main__':
    main()
