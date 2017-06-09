# table.py


def print_table(objects, colname):
    for col in colname:
        print("{:>10}".format(col), end=" ")
    print()

    for obj in objects:
        for col in colname:
            print("{:>10}".format(getattr(obj, col)), end=" ")
        print()

