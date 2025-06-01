# Title: Program #4
# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

"""
Program #4
Use the bios dataset.  Create a Python program to:
A. delete the born_date, born_city, born_region, died_date
B. create a new column called "power" which is the product of height_cm * weight_kg
C. sort the data in descending order of "power"
"""

import pandas as pd


def main():
    file_path = "bios.csv"

    # Read file in
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return

    # Make sure columns exist before operating
    for i in ['height_cm', 'weight_kg']:
        if i not in data.columns:
            print(f"Column {i} is not present in data")
            return

    data.drop(columns=['born_date', 'born_city', 'born_region', 'died_date'], inplace=True)

    data['power'] = data['height_cm'] * data['weight_kg']

    sorted_data = data.sort_values(by='power', ascending=False)

    sorted_data.to_csv("bios_edited.csv", index=False)  # Save for program 5
    print(sorted_data)
    print("Data saved.")

# Call the main function
if __name__ == '__main__':
    main()
