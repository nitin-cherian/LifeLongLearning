#iterators.py

print("""
iterator is an object which implements the __next__ method. So when next() function is invoked on the iterator,
it in-turn call the __next__ method to give the next item.
""")

print('Writing a iterator that keeps on giving the next integer without stopping')
print("""
{code}
class InfiniteIterator:
    def __init__(self):
        self.__int = 0

    def __next__(self):
        self.__int += 1
        return self.__int


i = InfiniteIterator()
print(next(i))

print(next(i))

print(next(i))

print(next(i))
{code}
""")


class InfiniteIterator:
    def __init__(self):
        self.__int = 0

    def __next__(self):
        self.__int += 1
        return self.__int


i = InfiniteIterator()
print(next(i))

print(next(i))

print(next(i))

print(next(i))



