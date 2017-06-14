# loop_over_2_lists.py


names = ["Eiffel Tower", "Empire State", "Sears Tower"]
heights = [324, 381, 442]


# The bad way
# for i in range(len(names)):
#     name = names[i]
#     height = heights[i]
#
#     print("{} : {}".format(name, height))


# The Pythonic way
for name, height in zip(names, heights):
    print("{} : {}".format(name, height))

# dict() can take a stream of pairs to produce a dictionary
print(dict(zip(names, heights)))
