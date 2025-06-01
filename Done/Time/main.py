# Title: Time
# Mid-term Challenge
# Starting Out With Python, 5th Edition
# Date: 3/4/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Declare vars
    seconds_in = None

    while not (seconds_in == 'q' or seconds_in == 'Q'):
        # Prompt input
        print('This program converts a large number of seconds to "Hours : Minutes : Seconds" format.')
        print('Type Q to quit.')
        seconds_in = input("Enter a number of seconds to convert : ")
        print()

        try:
            print(f'{sec_4mat(seconds_in)}')
        except ValueError:
            print("Input appears to be text, not a number. Please try again.")

    print(f"User typed '{seconds_in}' and program quit.")


def sec_4mat(seconds):
    # Convert arg to float
    seconds = float(seconds)

    # Calc
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60

    # Create string for output
    output = str(f"{hours:.0f} : {minutes:.0f} : {seconds:.0f}")

    # Return the string
    return output


# Call the main func
if __name__ == '__main__':
    main()
