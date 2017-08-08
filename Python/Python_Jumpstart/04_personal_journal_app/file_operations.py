# file_operations

"""
This module handles read and write on the journal file
"""
import os


def get_file_path(filename):
    file_path = os.path.join('.', 'data', filename)
    return file_path


def save(filename, entries):
    file_path = get_file_path(filename)
    try:
        with open(file_path, "w") as f:
            for entry in entries:
                f.write(entry + "\n")
        print("... saving to {}".format(os.path.abspath(file_path)))
        print("... saving complete.")
    except Exception as exc:
        print(str(exc))


def load(filename):
    file_path = get_file_path(filename)
    print("... loading from file {} ...".format(file_path))
    try:
        with open(file_path, "r") as f:
            for line in f:
                yield line.strip()
    except Exception as exc:
        print(str(exc))




