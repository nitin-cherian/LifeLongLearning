# iterators_should_be_iterable


print('''
According to the official doc:

*********
Iterators should implement the __iter__ method that returns the  iterator object itself,
so every iterator is also iterable and may be used in most places where other iterables
are accepted.
*********

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

hundredIter = HundredIterator()
print()

for i in hundredIter:
    print(i)
    
{code}
''')


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

hundredIter = HundredIterator()
print()

# for i in hundredIter:
#     print(i)


print("""Since the iterator has not implemented an __iter__ method, the iterator above is not 
 iterable and a for loop cannot be used on the iterator.
 To fix this issue, implement a __iter__ method on the iterator object, returning itself like so:.

{code}
class HundredIterator:
    def __init__(self):
        self.__int = 0

    def __iter__(self):
        return self

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

print()

hundredIter = HundredIterator()

for i in hundredIter:
    print(i)
{code}
""")


class HundredIterator:
    def __init__(self):
        self.__int = 0

    def __iter__(self):
        return self

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

print()

hundredIter = HundredIterator()

for i in hundredIter:
    print(i)



