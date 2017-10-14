# zip_unzip_iterables.py


mutants = ('charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pride')
powers = ('telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility')


zip_object = zip(mutants, powers)

# Print all the elements of the iterator zip_object all at once using a single instruction
# Use the * operator

print(*zip_object)


# Refilling the iterator as it was exhausted in the previous statement
zip_object = zip(mutants, powers)


# Unzipping to original tuples
result1, result2 = zip(*zip_object)   # * -> unpacks the tuples, zip -> zips the tuples to give original tuples 

print(result1 == mutants)
print(result2 == powers)
