# Title: Program #5
# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

"""
Program #5
Use the new bios dataset from #4.  Create a Python program to:
A. prints the counts for each NOC value
B. sorts and prints the averages for the height_cm by NOC
C. sorts and prints the averages of power based upon the NOC
"""

import pandas as pd


def main():
    file_path = "bios_edited.csv"

    # Read file in
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return

    # Make sure columns exist before operating
    for i in ['NOC', 'height_cm', 'power']:
        if i not in data.columns:
            print(f"Column {i} is not present in data")
            return

    noc_counts = data['NOC'].value_counts()
    print("Counts for each NOC value:")
    print(noc_counts)

    avg_height_by_noc = data.groupby('NOC')['height_cm'].mean().sort_values()
    print("\n\nAverages for height_cm by NOC (sorted):")
    print(avg_height_by_noc)

    avg_power_by_noc = data.groupby('NOC')['power'].mean().sort_values()
    print("\n\nAverages for power by NOC (sorted):")
    print(avg_power_by_noc)


# Call the main function
if __name__ == '__main__':
    main()
