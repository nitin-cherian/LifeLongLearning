# iterator_protocol.py


print("""
The iterator protocol specifies two special methods to be implemented for any object to allow iteration

1. For any object to be iterated over, it must implement the __iter__ method which returns an iterator object.
Any object that returns an iterator is an iterable.

2. An iterator must implement the __next__ method which returns the next item when called. This method should raise
StopIteration exception when items are exhausted.

3. An iterator must also implement __iter__ method returning self, so that it behaves like an iterable.
""")
