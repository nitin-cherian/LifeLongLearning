# sql-search.py - perform aggregation(MIN, MAX, SUM, AVG)


# import sqlite3 library
import sqlite3


# This function calculates the minimum of numbers in the table
import sys


def min_(c):
    c.execute("SELECT MIN(num) from numbers")
    result = c.fetchone()

    return result[0]


# This function calculates the maximum of numbers in the table
def max_(c):
    c.execute("SELECT MAX(num) from numbers")
    result = c.fetchone()

    return result[0]


# This function calculates the average of numbers in the table
def avg(c):
    c.execute("SELECT avg(num) from numbers")
    result = c.fetchone()

    return result[0]


# This function calculates the sum of numbers in the table
def sum_(c):
    c.execute("SELECT sum(num) from numbers")
    result = c.fetchone()

    return result[0]


# This function exits the program
def quit_(c):
    print('Exiting from the program...')
    sys.exit(0)


# Create a dictionary for mapping input to functions
aggregations = {
    '1': min_,
    '2': max_,
    '3': avg,
    '4': sum_,
    '5': quit_
}


# Run an infinite loop
def main(c):
    while True:
        print("""1. MIN\n2. MAX\n3. AVG\n4. SUM\n5. QUIT""")
        request = input("\n>>> ")

        # invoke the handlers for the request
        handler = aggregations.get(request, None)
        if not handler:
            print('Invalid input...Try again')
            continue

        result = handler(c)
        print(result)


# Start main
if __name__ == '__main__':
    with sqlite3.connect('newnum.db') as connection:
        c = connection.cursor()
        main(c)

