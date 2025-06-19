# Final Project
# Starting Out With Python, 5th Edition
# Date: 2/15/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

import sqlite3
#from pathlib import Path

filename = str(input("Filename/path to open: "))

conn = sqlite3.connect(filename)
cur = conn.cursor()
print("Database Initialized")


def cool_kill():
    conn.commit()  # Commit changes
    conn.close()  # Close the connector
    print("Database closed")


def cool_save():
    conn.commit()
    print("Database saved")


def get_table_data(table_name, column_name, condition=None):
    if condition is None:
        where_clause = ''
    else:
        where_clause = (' WHERE ' + str(condition))
    cur.execute(f'SELECT {str(column_name)} FROM {str(table_name)} {where_clause}')
    return cur.fetchall()


def get_column_info(table_name):
    cur.execute(f'PRAGMA table_info({str(table_name)})')
    return cur.fetchall()


def get_column_list(table_name):
    # Get column info
    info = get_column_info(table_name)

    # Pull only the names
    columns = []
    for x in info:
        columns.append(x[1])

    return columns


def get_table_info():
    cur.execute('PRAGMA table_list')
    return cur.fetchall()


def get_table_list(hide_internal=True):
    # Get table info
    info = get_table_info()

    # Pull only the table names
    tables = []
    for x in info:
        tables.append(x[1])

    # Strip internal tables if specified
    if hide_internal is True:
        tables.remove("sqlite_sequence")
        tables.remove("sqlite_schema")
        tables.remove("sqlite_temp_schema")

    return tables


# NOTE: This function errors when trying to insert a pre-existing entry.
def create_entry(table_name, data):
    # Get Data
    #  & Conv 2 a tuple. This is a hacky solution that
    # makes it work in SQLite.
    column_list = tuple(get_column_list(table_name))
    data = tuple(data)

    # Technically it's possible to insert multiple rows with this command,
    # although I'd refrain from doing that.
    cur.execute(f'INSERT INTO {table_name} {column_list} VALUES {data}')

    # Save the update. Is this necessary?
    cool_save()


def delete_table_entry(table_name, data):
    # Get Data
    #  & Conv 2 a tuple. This is a hacky solution that
    # makes it work in SQLite.
    column_list = tuple(get_column_list(table_name))
    data = tuple(data)

    # Generate the WHERE clause in the SQL statement
    where_clause = ""
    for x in range(len(column_list)):
        where_clause += f"{column_list[x]} = '{data[x]}'"
        if x + 1 < len(column_list):
            where_clause += ' AND '

    # Translate Python "None" to SQL "NULL"
    where_clause = where_clause.replace("= 'None'", "IS NULL")

    # Delete the entry
    cur.execute(f"DELETE FROM {str(table_name)} WHERE {where_clause}")

    # Save
    cool_save()


def update_table_entry(table_name, new_data, old_data):
    # Get Data
    #  & Conv 2 a tuple. This is a hacky solution that
    # makes it work in SQLite.
    column_list = tuple(get_column_list(table_name))
    new_data = tuple(new_data)
    old_data = tuple(old_data)

    # Generate the SET clause in the SQL statement
    set_clause = ""
    for x in range(len(column_list)):
        set_clause += f"{column_list[x]} = '{new_data[x]}'"
        if x + 1 < len(column_list):
            set_clause += ', '

    # Generate the WHERE clause in the SQL statement
    where_clause = ""
    for x in range(len(column_list)):
        where_clause += f"{column_list[x]} = '{old_data[x]}'"
        if x + 1 < len(column_list):
            where_clause += ' AND '

    # Translate Python "None" to SQL "NULL"
    # set_clause = set_clause.replace("''", "NULL")
    where_clause = where_clause.replace("= 'None'", "IS NULL")

    print(set_clause)
    print(where_clause)
    print(f'UPDATE {str(table_name)} SET {set_clause} WHERE {where_clause}')

    # Replace the entry
    cur.execute(f'UPDATE {str(table_name)} SET {set_clause} WHERE {where_clause}')

    # Save
    cool_save()


def create_table(table_name):
    # Convert inputs
    # Technically not needed
    # table_name = str(table_name)

    # Run the cmd
    cur.execute(f'CREATE TABLE {table_name} ({table_name}Id INTEGER PRIMARY KEY NOT NULL, {table_name}Name TEXT)')


def create_column(table_name, column_name):
    cur.execute(f'ALTER TABLE {table_name} ADD {column_name} TEXT')


def remove_table(table_name):
    cur.execute(f'DROP TABLE {table_name}')


def remove_column(table_name, column_name):
    cur.execute(f'ALTER TABLE {table_name} DROP {column_name}')


def get_table_entry(table_name, column_names):
    pass


def get_table_field(table, column, field):
    pass


def set_table(table):
    pass


def set_entry():
    pass


def set_field():
    pass


def set_column_name():
    pass


def search_table_name(table):
    pass


def search_column_name(table, column):
    pass


def search_entry(table, entry):
    pass
