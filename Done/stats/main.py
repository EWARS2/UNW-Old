# Title: Calc stats from list
# In-class Exercise
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

import statistics

def main():
    # Define
    exam_grades = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # Calculate
    average = statistics.mean(exam_grades)
    minimum = min(exam_grades)
    maximum = max(exam_grades)

    # Display
    print(f'Average: {average}')
    print(f'Minimum: {minimum}')
    print(f'Maximum: {maximum}')


# Call the main func
if __name__ == '__main__':
    main()