# as_01_sql - insert random integers


# import modules
import sqlite3
import random


with sqlite3.connect('newnum.db') as connection:
    c = connection.cursor()

    # DROP TABLE
    c.execute("DROP TABLE IF EXISTS numbers")

    # CREATE TABLE
    c.execute("CREATE TABLE numbers (num INT)")

    # Insert 100 random integers into the table
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0, 100),))
