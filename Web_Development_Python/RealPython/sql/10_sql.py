# create a table and populate it with data


# import sqlite3 library
import sqlite3


with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS regions(city TEXT, region TEXT)")

    cities = [
        ('New York City', 'Northeast'),
        ('San Francisco', 'West'),
        ('Chicago', 'Midwest'),
        ('Houston', 'South'),
        ('Phoenix', 'West'),
        ('Boston', 'Northeast'),
        ('Los Angeles', 'West'),
        ('Houston', 'South'),
        ('Philadelphia', 'Northeast'),
        ('San Antonio', 'South'),
        ('San Diego', 'West'),
        ('Dallas', 'South'),
        ('San Jose', 'West'),
        ('Jacksonville', 'South'),
        ('Indianapolis', 'Midwest'),
        ('Austin', 'South'),
        ('Detroit', 'Midwest')
    ]

    cursor.executemany("INSERT INTO regions VALUES(?, ?)", cities)

    cursor.execute("SELECT * from regions ORDER BY region ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row[0], row[1])


