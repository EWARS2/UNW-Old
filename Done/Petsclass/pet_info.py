# Title: Ch10Ex: Pet_info.py Petscop pt 2
# In-class program
# Starting Out With Python, 5th Edition
# Date: 3/18/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

from pets import Pet


def main():
    # Local vars
    pet_name = ""
    pet_type = ""
    pet_age = 0

    # Get pet data
    pet_name = input("Pet name: ")
    pet_type = input("Type of animal: ")
    pet_age = int(input("Pet's Age: "))
    print()

    # Create a pet instance
    mypet = Pet(pet_name, pet_type, pet_age)

    print("Info on this pet:")
    print(f"Pet Name: {mypet.get_name()}")
    print(f"Animal Type: {mypet.get_animal_type()}")
    print(f"Age of Pet: {mypet.get_age()}")


# Call the main func
if __name__ == '__main__':
    main()