# Title: Cities
# In-class Exercise
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Define
    cities = ['Bettyston', 'Minneapolis']

    # Get input
    prompt = str(input('Where would you NOT like to go? : '))

    # Errors out if item is not in list
    try:
        # Get more input
        new_entry = str(input('Enter desired city to replace: '))

        # Get the index
        prompt_index = cities.index(prompt)
        # Replace the entry
        cities[prompt_index] = new_entry

        # Display
        print("Here's the new cities list:")
        print(cities)

    except ValueError:
        print(f'The entry {prompt} was not found in the list.')


# Call the main func
if __name__ == '__main__':
    main()
