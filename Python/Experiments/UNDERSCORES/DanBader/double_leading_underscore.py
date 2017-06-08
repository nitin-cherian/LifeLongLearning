# double_leading_underscore.py


print("""
1. Python interpreter treats double underscore prefix names(variable and methods) in classes differently.
2. Python rewrites the names with double underscore prefix to avoid name conflicts in subclasses -- name mangling
3. Name mangling happens only in class context

class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 35

t = Test()
print(dir(t))

""")


class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 35

t = Test()
print(dir(t))

print("""
In the above example, we see foo, _bar but not __baz. 
Name mangling happened and __baz became _Test__baz
""")


class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = "overriden"
        self._bar = "overriden"
        self.__baz = "overriden"


e = ExtendedTest()
print(dir(e))
print(e.foo)
print(e._bar)
print(e._ExtendedTest__baz)
print(e._Test__baz)
# print(e.__baz)

print("""
Name mangling is fully transparent to the user
----------------------------------------------
""")


class ManglingTest:
    def __init__(self):
        self.__mangled = 45

    def get_mangled(self):
        return self.__mangled


m = ManglingTest()
print(m.get_mangled())
# print(m.__mangled())

print("""
Name mangling applies to method names also
------------------------------------------
""")


class ManglingMethodTest:
    def __mangling_method(self):
        return "hello"

    def call_mangling(self):
        return self.__mangling_method()

mm = ManglingMethodTest()
print(mm.call_mangling())
# print(mm.__mangling_method())


print('''
The Mangling trick
------------------
''')

_ManglingGlobal__mangled = 50

class ManglingGlobal:
    def get_mangled(self):
        return __mangled

mg = ManglingGlobal()
print(mg.get_mangled())

print("""
In the above example, the name of the global variable was deliberately mangledi by me. When __mangled inside the Class is seen by Python 
interpreter, it re-writes it to a mangled name which matches with the name of the global variable. 
""")



