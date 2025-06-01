# Title: Program #6
# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

"""
Program #6
Write a python program to clean the Athlete Event dataset.
You should remove rows that have weird or significantly missing data.
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
    for i in ['Age', 'Height', 'Weight', 'Year']:
        if i not in data.columns:
            print(f"Column {i} is not present in data")
            return

    print("Original Data Info:")
    print(data.info())

    # Remove rows with significantly missing data
    threshold = int(0.7 * data.shape[1])  # 70%
    data_cleaned = data.dropna(thresh=threshold)

    # Drop entries with negative or zero values.
    data_cleaned = data_cleaned[data_cleaned['Age'] > 0]
    data_cleaned = data_cleaned[data_cleaned['Height'] > 0]
    data_cleaned = data_cleaned[data_cleaned['Weight'] > 0]
    data_cleaned = data_cleaned[data_cleaned['Year'] > 0]

    print("\n\nCleaned Data Info:")
    print(data_cleaned.info())

    output_file_path = "athlete_events_edited.csv"
    data_cleaned.to_csv(output_file_path, index=False)
    print(f"\nCleaned dataset saved to '{output_file_path}'.")


# Call the main function
if __name__ == '__main__':
    main()
