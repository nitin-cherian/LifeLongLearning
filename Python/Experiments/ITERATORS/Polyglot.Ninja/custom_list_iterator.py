# custom_list_iterator.py


class CustomList:
    def __init__(self, a_list):
        self.elements = a_list

    def __iter__(self):
        return CustomListIterator(self)


class CustomListIterator:
    def __init__(self, custom_list):
        self.custom_list = custom_list
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.custom_list.elements):
            item = self.custom_list.elements[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration

# using the custom list iterable to create a list
my_list = CustomList([1, 2, 3, 4])
# looping through the custom list iterable
for e in my_list:
    print(e)
print("**************")
# using the custom list iterable to create another list
my_list1 = CustomList([10, 20, 30, 40])
# looping through the custom list iterable
for e in my_list1:
    print(e)
print("**************")
# using the custom list iterator
my_list_iterator = CustomListIterator(my_list)
for e in my_list_iterator:
    print(e)
print("**************")
# When the items are exhausted, the custom list iterator raises StopIteration
print(next(my_list_iterator))
print("**************")
