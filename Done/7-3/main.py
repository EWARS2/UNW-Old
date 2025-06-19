# Title: Rainfall Statistics
# Chapter 7, Exercise 3 
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith



def main():
    # Create list
    temps = []

    # Populate list
    for month in range(1,13):
        temps.append(float(input(f'Temperature on month {month}:')))

    # Calculate
    total = sum(temps)
    avg = total/month
    minimum = min(temps)
    maximum = max(temps)

    # Display results
    print(f'\n{temps}')
    print(f'Total: {total}')
    print(f'Average: {avg}')
    print(f'Lowest: {minimum}')
    print(f'Highest: {maximum}')


# Call the main func
if __name__ == '__main__':
    main()
