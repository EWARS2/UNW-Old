# Title: Program #1
# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

"""
Program #1
Create a Python program that will access and display the first 5 and last 5 rows of the Athlete Events dataset.
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

    print("First 5 rows:")
    print(data.head())  # Default is 5
    print("\nLast 5 rows:")
    print(data.tail())  # Default is 5

# Call the main function
if __name__ == '__main__':
    main()
