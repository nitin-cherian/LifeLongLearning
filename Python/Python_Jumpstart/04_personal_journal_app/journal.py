# journal.py

"""
A personal journal app. This app loads the journal entries from a file at startup. User can list the entries, add new 
entries or exit from the app. When the app exits, the journal will be saved to the file
to be loaded again at app startup
"""
from file_operations import save, load


def print_header():
    print("--------------------------------")
    print("      PERSONAL JOURNAL APP")
    print("--------------------------------")


def list_entry(entries):
    print("Your {} journal entries".format(len(entries)))
    print()

    for index, entry in enumerate(entries, start=1):
        print("[{}]* {}".format(index, entry))


def add_entry(journal):
    print('Enter your journal entry:')
    entry = input()
    journal.append(entry)


def main():
    print_header()
    journal = "default.jrl"
    entries = [entry for entry in load(journal)]
    print("... loaded {} entries ...".format(len(entries)))

    while True:
        user_input = input("What do you want to do? [L]ist, [A]dd or E[x]it: ")
        user_input = user_input.strip().lower()

        if user_input == 'l':
            list_entry(entries)
        elif user_input == 'a':
            add_entry(entries)
        elif user_input == 'x':
            save(journal, entries)
            break
        else:
            continue

        print()


if __name__ == '__main__':
    main()
