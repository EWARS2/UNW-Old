# Title: Program #2
# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

"""
Program #2
Create a Python program that will print the following things from the Athlete Events dataset:
    the fifth row of the data,
    the second column of the data,
    only the rows that have NOC = Nigeria.
"""

import pandas as pd


def main():
    file_path = "athlete_events.csv"

    # Read file in
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return

    # Make sure columns exist before operating
    for i in ['NOC']:
        if i not in data.columns:
            print(f"Column {i} is not present in data")
            return

    print("5th Row:")
    fifth_row = data.iloc[4]
    print(fifth_row)

    print("\n\n2nd Column:")
    second_column = data.iloc[:, 1]
    print(second_column)

    print("\n\nRows where NOC = Nigeria:")
    nigeria_data = data[data['NOC'] == 'NGR']
    print(nigeria_data)


# Call the main function
if __name__ == '__main__':
    main()
