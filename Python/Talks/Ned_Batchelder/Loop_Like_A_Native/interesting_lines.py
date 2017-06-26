# interesting_lines.py


def interesting_lines(f):
    for line in f:
        if line.startswith("#"):
            continue

        line = line.strip()

        if not line:   # Empty line
            continue

        yield line

with open('myconfig.ini') as f:
    for line in interesting_lines(f):
        print(line)
