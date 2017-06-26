# loop_like_a_native.py


print("""
1. Lot of things in Python are iterables

    -- List --> gives elements if iterated
    -- String --> gives characters if iterated
    -- Dictionary --> gives keys if iterated
    -- file --> gives lines
""")

for l in "hello":
    print(l)
print("***********")

for e in [1, 2, 3, 4, 5]:
    print(e)
print("***********")

d = {1: "a", 2: "b", 3: "c", 4: "d"}
for k in d:
    print(k)
print("***********")

for v in d.values():
    print(v)
print("***********")

for k, v in d.items():
    print(k, v)
print("***********")

with open('text', "r") as f:
    for line in f:
        print(line)

print("""
Other uses of iterables
-----------------------
1. Python can do interesting things with iterables
    
    list function
    -------------
    new_list = list(iterable)
    -- list function takes an iterable, pulls out items from iterable one by one and returns a list
    
    list comprehension
    ------------------
    results = [f(x) for x in iterable]
    
    sum function
    ------------
    total = sum(iterable)
    -- takes an iterable with items that can be added together and returns the sum
    
    >>> sum([1, 2, 3, 4])
    10
    >>> sum((1, 2, 3, 4))
    10
    >>> d = {'a': 1, 'b': 2, 'c': 3}
    >>> sum(d)
    Traceback (most recent call last):
      File "/usr/lib/python3.5/code.py", line 91, in runcode
        exec(code, self.locals)
      File "<input>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>> d = {1: 'a', 2: 'b', 3: 'c'}
    >>> sum(d)
    6
    >>> d = {'a': 1, 'b': 2, 'c': 3}
    >>> sum(d.values())
    6
    
    min, max functions
    ------------------
    takes iterables of comparable values (integer or string) and gives smallest or greatest value
    
    >>> max([1, 2, 3, 4])
    4
    >>> min(1, 2, 3, 4)
    1
    >>> d = {1: 'a', 2: 'b', 3: 'c'}
    >>> min(d)
    1
    >>> min(d.values())
    'a'
    >>> max(d)
    3
    >>> max(d.values())
    'c'
    >>> d = {1: ['a', 'b'], 2: ['c', 'd'] , 3: ['e', 'f']}
    >>> max(d.values())
    ['e', 'f']
    >>> d = {1: {'a': 'b'}, 2: {'c': 'd'} , 3: {'e': 'f'}}
    >>> max(d.values())
    Traceback (most recent call last):
      File "/usr/lib/python3.5/code.py", line 91, in runcode
        exec(code, self.locals)
      File "<input>", line 1, in <module>
    TypeError: unorderable types: dict() > dict()

    join function
    -------------
    takes an iterable of strings and joins them all together
    -- combined = "".join(iterable)
    
    >>> "".join([1, 2, 3, 4])
    Traceback (most recent call last):
      File "/usr/lib/python3.5/code.py", line 91, in runcode
        exec(code, self.locals)
      File "<input>", line 1, in <module>
    TypeError: sequence item 0: expected str instance, int found
    >>> "".join(['1', '2', '3', '4'])
    '1234'
    >>> "".join('1', '2', '3', '4')
    Traceback (most recent call last):
      File "/usr/lib/python3.5/code.py", line 91, in runcode
        exec(code, self.locals)
      File "<input>", line 1, in <module>
    TypeError: join() takes exactly one argument (4 given)
    >>> "".join(('1', '2', '3', '4'))
    '1234'
    >>> d = {1: 'a', 2: 'b', 3: 'c'}
    >>> "".join(d)
    Traceback (most recent call last):
      File "/usr/lib/python3.5/code.py", line 91, in runcode
        exec(code, self.locals)
      File "<input>", line 1, in <module>
    TypeError: sequence item 0: expected str instance, int found
    >>> "".join(d.values())
    'abc'

    Takeaway
    --------
    
    1. with iterables, we can loop over data without using explicit loop(ex: for-loop)
    2. loop is implicit in the function
    
""")

print("""
enumerate function
------------------

1. Indexing does not work on many iterables like set, dictionary, files etc.

So we cannot use

for i in range(len(iterable)):
   print i, iterable[i]
   
    >>> my_set = {'a', 'b', 'c'}
    >>> for i in range(len(my_set)):
    ...     print(i, my_set[i])   
    ...     
    Traceback (most recent call last):
      File "/usr/lib/python3.5/code.py", line 91, in runcode
        exec(code, self.locals)
      File "<input>", line 2, in <module>
    TypeError: 'set' object does not support indexing
    
    
    >>> for i, element in enumerate(my_set, start=1):
    ...     print(i, element)
    ...     
    1 a
    2 c
    3 b    
""")


print("""
Loop over two list at the same time
-----------------------------------
    -- Refer loop_over_2_lists.py
    -- use the zip function
    -- zip function:
        -- takes a pair of streams and produces a stream of pairs.
    -- the dict() constructor accepts a stream of pairs to create a dictionary
""")

print("""
max() function on dict
----------------------

    -- Refer max_function_on_dict.py
    -- max function iterates through the first parameter, it can be values, items or keys and returns the value, item or key based on the key function
    -- what is passed as parameter to the key function during each iteration is the first parameter of max function(can be values, items or keys) 
""")

print("""
Generators
----------
    -- when invoked returns an iterator
    -- when the returned iterator is iterated, it runs the statements in the generator and whenever the yield keyword 
    is hit, it produces one more value.
    -- kind of a function which can keep producing values over and over.
    -- a simple generator, refer simple_generator.py
    -- an evens generator, refer even_generator.py
    -- abstracting iteration
       eg: iterating a file to get the lines which are not blank and lines not startswith pound(#)
       refer interesting_lines.py 
""")

print("""
Low level iteration
-------------------
    -- iterable: any value that produces a stream of values
    -- iterator: an object that knows where you are in that stream.
    -- a book full of pages is an iterable, and bookmark is an iterator. 
        -- a book can have multiple bookmarks, similarly an iterable can have multiple iterators
        
    iterator = iter(iterable)
    value = next(iterator)
    value = next(iterator)
    ..
    ..
    ..
""")
