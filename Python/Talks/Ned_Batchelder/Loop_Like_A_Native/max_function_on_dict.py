# max_function_on_dict


tall_buildings = {
    "Empire State": 381, "Sears Tower": 442,
    "Burj Khalifa": 828, "Taipei 101": 509
}


# find the height of the tallest building
print("Height of the tallest building: ", max(tall_buildings.values()))


# find the name, height pair that is tallest
# print(max(tall_buildings.items()))  # This will find the max based on the name not the height
print(max(tall_buildings.items(), key=lambda b: b[1]))


# find the tallest building
print(max(tall_buildings, key=tall_buildings.get))

