# why_iterables.py


print("""
Iterator behaves like an iterable in that it implements the __iter__ method. Then why do we need iterables?
When StopIteration is raised from an iterator, there is no way to iterator over the iterator again, because
iterator maintains the state and return self when iter is invoked on it. If we iterate over iterables, a fresh instance 
of iterator is returned which can be used to iterate again. This is what happens in the case of iterables like 'list'
""")



