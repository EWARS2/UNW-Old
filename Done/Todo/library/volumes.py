# Proposal Project
# Starting Out With Python, 5th Edition
# Date: 2/27/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

import sqlite3 as lite
import sys

# Use the conn connector to connect SQLite to the volumes database
conn = lite.connect('volumes.db')


def print_rows(arg_rows):
    # Loop through the rows that were selected; print each row
    for row in arg_rows:
        print(row)
    print()


with conn:
    # Create a cursor
    cur = conn.cursor()

    # Execute the SQL statement
    cur.execute("SELECT * FROM author")

    # fetchall method retrieves all rows in table
    rows = cur.fetchall()

    print_rows(rows)


# Close the connector
conn.close()