# SQlite functions


# import sqlite3 library
import sqlite3


with sqlite3.connect('new.db') as connection:
    c = connection.cursor()

    # create a dictionary of sql queries
    sql = {
        'average': "SELECT avg(population) from population",
        'maximum': "SELECT max(population) from population",
        "minimum": "SELECT min(population) from population",
        "sum": "SELECT sum(population) from population",
        "count": "SELECT count(city) from population"
    }

    for key, value in sql.items():
        c.execute(value)

        # fetchone retrieves one record from the query
        result = c.fetchone()

        # output the result to screen
        print(key, " = ", result[0])


