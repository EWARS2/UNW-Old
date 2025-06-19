# Title: Average Rainfall
# Chapter 4, Exercise 5
# Starting Out With Python, 5th Edition
# Date: 2/7/2024, Updated 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

def main():
    # Get number of years for input
    in_years = int(round(float(input('Iterate for how many years? : '))))
    
    rainfall_avg(in_years)


def rainfall_avg(years):
    # Declare variables 
    MONTHS_IN_YR = 12
    total_rainfall = 0
    total_month = 0

    # Repeat every month for every year
    for year_counter in range(years):
        for month_counter in range(MONTHS_IN_YR):
            # Increment month counter
            total_month += 1

            # Display the prompted month
            print(f'\nYear:{year_counter+1} Month:{month_counter+1} Overall Month:{total_month}')

            # Add the new entry
            total_rainfall += float(input(f'Inches of rainfall for month: '))

    # Calculate average
    final_average = total_rainfall / total_month

    # Print results with formatting
    print(f'\n Total rainfall of {total_rainfall} Inches.')
    print(f' Average rainfall of {final_average} Inches, spanning {total_month} Months')


# Call the main func
if __name__ == '__main__':
    main()
