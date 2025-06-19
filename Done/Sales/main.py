# Title: Sales
# In-class Exercise
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

import statistics


def main():
    # Define
    scores = [[175, 200, 350, 450, 500],
              [176, 200, 350, 450, 500],
              [169, 200, 350, 450, 500],
              [100, 200, 350, 450, 500]]

    # Calc & Disp
    for i in range(len(scores)):
        avg = statistics.mean(scores[i])
        print(avg)


# Call the main func
if __name__ == '__main__':
    main()