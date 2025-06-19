# Final Project
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

# Input MUST be in either a list or a tuple,
# Otherwise the code will create a new cell
# for every letter in a string,
# or just fail with other data types.
def list2csv(contents, file_name):
    # Open the file
    file_pointer = open(str(file_name), 'w')

    # Loop through the entries
    for y in contents:
        for x in y:
            # Removes colons so as not to break the CSV format
            entry = str(x).replace(",", " ")

            file_pointer.write(entry + ",")
        file_pointer.write("\n")

    print(f"Successfully exported {file_name}")
    file_pointer.close()


def test():
    test_list = [("Entry 1", "Entry 2", "Entry 3"),
                 ["Entry 11", "Entry 12", "Entry 13"],
                 ["Entry 21", "Entry 22", "Entry 23"],
                 ["Entry 69,420"],
                 "John Johnson",
                 ]
    list2csv(test_list, "test.csv")


if __name__ == '__main__':
    test()
