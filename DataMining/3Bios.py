# Title: Program #3
# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

"""
Program #3
Create a Python program to sort the Bios dataset by the following things:
name (in alphabetical order),
weight (from largest to smallest),
died_date (in chronological order).
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
    for i in ['name', 'weight_kg', 'died_date']:
        if i not in data.columns:
            print(f"Column {i} is not present in data")
            return

    sorted_by_name = data.sort_values(by='name')
    print("Dataset sorted by Name (alphabetical order):")
    print(sorted_by_name)

    sorted_by_weight = data.sort_values(by='weight_kg', ascending=False)
    print("\n\nDataset sorted by Weight (largest to smallest):")
    print(sorted_by_weight)

    # data['died_date'] = pd.to_datetime(data['died_date'], errors='coerce')
    sorted_by_died_date = data.sort_values(by='died_date')
    print("\n\nDataset sorted by Died Date (chronological order):")
    print(sorted_by_died_date)

    sorted_by_all = data.sort_values(by=['name', 'weight_kg', 'died_date'], ascending=[True, False, True])
    print("\n\nDataset sorted by all three:")
    print(sorted_by_all)


# Call the main function
if __name__ == '__main__':
    main()
