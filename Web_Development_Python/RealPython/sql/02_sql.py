# INSERT command


# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# insert date
cursor.execute("INSERT INTO population VALUES ('New York City', \
               'NY', 840000000)")
cursor.execute("INSERT INTO population VALUES ('San Francisco', \
                'CA', 8000000)")

# commit the changes
conn.commit()

# close the database connection
conn.close()

