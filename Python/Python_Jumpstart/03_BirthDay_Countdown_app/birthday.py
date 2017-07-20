# birthday.py
import datetime
from collections import namedtuple

Date = namedtuple('Date', ['year', 'month', 'day'])


def print_header():
    """ Print the header for this app"""
    print("--------------------------------------")
    print("        BIRTHDAY COUNTDOWN APP")
    print("--------------------------------------")


def get_user_bday():
    """ Get year, month and day as strings from user """
    year = input("Enter your year of birth(YYYY): ")
    month = input("Enter your month of birth(MM): ")
    day = input("Enter your day of birth(DD): ")

    # Strip the whitespaces and convert to integers
    year = int(year.strip())
    month = int(month.strip())
    day = int(day.strip())

    return Date(year, month, day)


def calculate_days(bday):
    """ Calculate the number of days until the user's birthday """
    now = datetime.datetime.now()
    diff = now - datetime.datetime(now.year, bday.month, bday.day)
    days = int(diff.total_seconds() / 60 / 60 / 24)

    return days


def print_result(bday, days):
    """ Print the result to the user """
    print("Looks like you were born on {}/{}/{}".format(bday[0], bday[1], bday[2]))
    if days > 0:
        print("You celebrated your birthday {} days before".format(days))
    elif days < 0:
        print("You will celebrate your birthday in {} days".format(-days))
    else:
        print("Today is your birthday. Happy Birthday! Have a great one!")

    pass


def main():
    print_header()
    bday = get_user_bday()
    days = calculate_days(bday)
    print_result(bday, days)

if __name__ == '__main__':
    main()
