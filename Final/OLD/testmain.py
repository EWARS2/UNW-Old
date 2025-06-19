# Final Project
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

from coollibsqlite import *
from coollibexport import *
# from coollibui import *


def main():
    #print(get_table_data("Clients", "*", "ClientID = 1"))
    #print(get_table_data("Clients", "*"))
    #print(get_table_list())
    #print(get_column_list("Clients"))

    #the_data = get_table_data("Clients", "*")
    #print(the_data)
    #list2csv(the_data, "test.csv")

    #delete_table_entry("Clients", ["70", "Pizza", "Pleb"])
    #print(get_table_data("Clients", "*"))

    update_table_entry("Clients", ["54", "None", "Bean"], ["54", "B", "None"])



# Call the main func
if __name__ == '__main__':
    main()
    cool_kill()
    print("Successfully succeeded in succeeding.")
