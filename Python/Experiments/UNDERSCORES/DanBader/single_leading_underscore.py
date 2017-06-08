# single_leading_underscore.py


print("""
Single leading underscore: _var
-------------------------------
1. When applied to variable and method names, it has a meaning by convention only.
2. Intended as a hint to the programmer that it is used for internal purposes, but not enforced by Python.
3. Does not affect the behaviour of the program.
""")

print("""
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23

t = Test()
print(t.foo)
print(t._bar)
""")


class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23

t = Test()
print("t.foo = ", t.foo)
print("t._bar = ", t._bar)

print("""
In the above example, we can see that putting single underscore before bar did not prevent the 
user from accessing it.
""")

print("""
Impact on module imports
------------------------
1. Wildcard import -- names with leading underscores are not imported.
2. Regular import -- names with leading underscores are also imported.
""")

print("""
def external_func():
    print("external func")


def _internal_func():
    print("internal func")
""")


def external_func():
    print("external_func")


def _internal_func():
    print("_internal_func")


print("""
In the example above, _internal_func is not imported on 'from single_leading_underscore import *'.
It will be imported on regular imports.
""")





