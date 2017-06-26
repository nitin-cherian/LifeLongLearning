# evens_generator.py


my_list = [20, 12, 43, 56, 77, 90, 87, 23, 54, 36, 74]


def do_something(num):
    print("do_something with", num)


# In this loop, we are doing 2 things: picking up evens and then do_something
for num in my_list:
    if num % 2 == 0:
        do_something(num)

print("********************")


# Better way: move the picking up evens into a separate function
def evens():
    numbers = []
    for num in my_list:
        if num % 2 == 0:
            numbers.append(num)  # will run out of space, if my_list is really big
    return numbers

for num in evens():
    do_something(num)

print("********************")


# Much better: use generators, because if the list is really big, we will not run out of space
def evens_generator():
    for num in my_list:
        if num % 2 == 0:
            yield num

for num in evens_generator():
    do_something(num)
