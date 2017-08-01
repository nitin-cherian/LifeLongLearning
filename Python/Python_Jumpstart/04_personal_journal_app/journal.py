# journal.py

"""
A personal journal app. This app loads the journal entries from a file at startup. User can list the entries, add new 
entries or exit from the app. From the app exits, the journal will be saved to the file
to be loaded again at app startup
"""


def print_header():
    print("--------------------------------")
    print("      PERSONAL JOURNAL APP")
    print("--------------------------------")


def main():
    print_header()

    while True:
        user_input = input("What do you want to do? [L]ist, [A]dd or E[x]it: ")
        print(user_input)

if __name__ == '__main__':
    main()
