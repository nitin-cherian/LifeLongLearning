# executemany method


# import sqlite3 library
import sqlite3


# use the with clause to avoid having to use commit and close statements explicitly
with sqlite3.connect("new.db") as connection:
    "create a cursor to execute sql commands"
    cursor = connection.cursor()

    # insert multiple records using list of tuples
    cities = [
        ('Boston', 'MA', 600000),
        ('Chicago', 'IL', 2700000),
        ('Houston', 'TX', 2100000),
        ('Phoenix', 'AZ', 1500000)
    ]

    # insert date into table
    cursor.executemany("""INSERT INTO population VALUES (?, ?, ?)""", cities)

