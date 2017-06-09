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