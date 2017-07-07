# executemany() method


# import sqlite3 library
import sqlite3


with sqlite3.connect('new.db') as connection:
    cursor = connection.cursor()

    # insert multiple entries using list of tuples
    cities = [
        ('Boston', 'MA', 600000),
        ('Los Angeles', 'CA', 38000000),
        ('Houston', 'TX', 2100000),
        ('Philadelphia', 'PA', 1500000),
        ('San Antonio', 'TX', 1400000),
        ('San Diego', 'CA', 130000),
        ('Dallas', 'TX', 1200000),
        ('San Jose', 'CA', 900000),
        ('Jacksonville', 'FL', 800000),
        ('Indianapolis', 'IN', 800000),
        ('Austin', 'TX', 800000),
        ('Detroit', 'MI', 700000)
    ]

    cursor.executemany("INSERT INTO population VALUES(?, ?, ?)", cities)

    cursor.execute("SELECT * from population WHERE population > 1000000")

    rows = cursor.fetchall()

    for row in rows:
        print(row[0], row[1], row[2])

