# Select records from techtime.db database

import sqlite3 as lite
import sys

conn = lite.connect('techtime.db')

with conn:
    cur = conn.cursor()

    cur.execute('INSERT INTO employee VALUES ("4", "Corrie", "ten Boom",  \
                            "101 Bartel St", "Roseville", "MN", "4/15/2024")')

    cur.execute('SELECT * FROM employee')

    rows = cur.fetchall()

    for row in rows:
        print(row)

    print()
    cur.execute('UPDATE employee SET city = "Shoreview"  \
                        WHERE emp_id = "3"')

    cur.execute('SELECT * FROM employee')

    rows = cur.fetchall()

    for row in rows:
        print(row)

    print()

    cur.execute('DELETE FROM employee WHERE emp_id = "1"')

    cur.execute('SELECT * FROM employee')

    rows = cur.fetchall()

    for row in rows:
        print(row)

conn.close()