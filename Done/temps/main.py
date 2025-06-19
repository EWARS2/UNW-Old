# Title: Python Temperature
# In-class exercise
# Starting Out With Python, 5th Edition
# Date: 2/21/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith


def main():
    # Create list
    temps = []

    # Populate list
    for day in range(1,8):
        temps.append(float(input(f'Temperature on day {day}:')))

    # Calculate
    total = sum(temps)
    avg = total/day

    # Display results
    print(f'\n{temps}')
    print(f'Total: {total}')
    print(f'Average: {avg}')


# Call the main function.
if __name__ == '__main__':
    main()