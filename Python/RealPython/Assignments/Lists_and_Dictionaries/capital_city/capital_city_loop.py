# capital_city_loop.py

"""
write a script that imports the capitals_dict variable along with the 'random'
package:

from capitals import capitals_dict
import random

This script should use a while loop to iterate through the dictionary and grab a random
state and capital, assigning each to a variable. The user is then asked what the capital of
the randomly picked state is. The loop continues forever, asking the user what the
capital is, unless the user either answers correctly or types "exit".
If the user answers correctly, "Correct" is displayed after the loop ends. However, if the
user exits without guessing correctly, the answer is displayed along with "Goodbye."

NOTE: Make sure the user is not punished for case sensitivity. In other words, a
guess of "Denver" is the same as "denver". The same rings true for exiting -
"EXIT" and "Exit" are the same as "exit".
"""

from capitals import capitals_dict
import random


def main():
    city, capital = random.choice(list(capitals_dict.items()))

    while True:
        print('What is the capital of {}?'.format(city))
        user_answer = input('>> ').lower().strip()

        if user_answer == capital.lower() or user_answer == 'exit':
            message = "Correct. Well Done!" if user_answer == capital.lower() \
                       else "The capital of {} is {}. Goodbye.".format(city, capital)
            break

        print()

    print(message)



if __name__ == '__main__':
    main()
