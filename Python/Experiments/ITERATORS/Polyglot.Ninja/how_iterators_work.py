# how_iterators_work.py

print("""
When we do for loop, how does it fetch one item at time?

 -- Two functions 'iter' and 'next' come into play

 -- 'iter' function is invoked on the iterable by the for loop. 
    This in-turn calls special method '__iter__' method of the iterable and returns an iterator.

 -- for loop then repeatedly calls 'next' on the iterator, which in-turn invokes the iterator's __next__ function, to 
    return one element of the iterable on every invocation until the 'StopIteration' exception is raised.
""")

l = [1, 2, 3]

i = iter(l)

print(type(l))
print(type(i))

print(next(i))
print(next(i))
print(next(i))

print("""
-- In the above example, l is a list and it is an iterable. 
-- An iterable is an object on which if 'iter' function is invoked returns and iterator.
""")

# print(next(i))

print("""Simulating for loop on an iterable using while loop
{code}
l = [1, 2, 3]
i = iter(l)

while True:
    try:
        item = next(i)
        print(item)
    except StopIteration:
        break
{code}        
""")
l = [1, 2, 3]
i = iter(l)

while True:
    try:
        item = next(i)
        print(item)
    except StopIteration:
        break

