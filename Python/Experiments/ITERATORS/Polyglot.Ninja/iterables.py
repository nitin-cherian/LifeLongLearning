# iterables.py

print("""
An iterable is any object that returns an iterator when iter() function is invoked on it.
""")

print("""Writing an iterable that repeatedly returns an integer without stopping
{code}
class InfiniteIterator:
    def __init__(self):
        self.__int = 0

    def __next__(self):
        self.__int += 1
        return self.__int


class InfiniteNumbers:
    def __iter__(self):
        return InfiniteIterator()


inf = InfiniteNumbers()


for i in inf:
    if i > 100:
        break

{code}
""")


class InfiniteIterator:
    def __init__(self):
        self.__int = 0

    def __next__(self):
        self.__int += 1
        return self.__int


class InfiniteNumbers:
    def __iter__(self):
        return InfiniteIterator()


inf = InfiniteNumbers()


for i in inf:
    if i > 100:
        break

    print(i)


print("""
Write an iterator that stop after giving 100 integers
{code}
class HundredIterator:
    def __init__(self):
        self.__int = 0

    def __next__(self):
        self.__int += 1

        if self.__int > 100:
            raise StopIteration

        return self.__int
    

class HundredIterable:
    def __iter__(self):
        return HundredIterator()

hundred = HundredIterable()

for i in hundred:
    print(i)
{code}
""")


class HundredIterator:
    def __init__(self):
        self.__int = 0

    def __next__(self):
        self.__int += 1

        if self.__int > 100:
            raise StopIteration

        return self.__int


class HundredIterable:
    def __iter__(self):
        return HundredIterator()

hundred = HundredIterable()

for i in hundred:
    print(i)
