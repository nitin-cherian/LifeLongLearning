# INSERT command with error handler


# import the sqlite3 library
import sqlite3


# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object to execute the commands
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8400000)")

    conn.commit()
except sqlite3.OperationalError as e:
    print('Operational Error: {}'.format(str(e)))

# close the database connection
conn.close()
