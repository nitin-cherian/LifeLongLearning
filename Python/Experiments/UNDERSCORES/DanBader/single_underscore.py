# single_underscore.py


print("""
1. Used as temporary variable as shown below:
""")

for _ in range(5):
    print("hello")


car = ('red', 'auto', 12, 3812.4)

color,_, _,mileage = car

print(color)
print(mileage)
print(_)   # will take the last value


print("""
2. Used a special variable in most Python REPL
>>> 20 + 3
23
>>> _
23
>>> print(_)
23

>>> list()
[]
>>> _.append(1)
>>> _.append(2)
>>> _.append(3)
>>> _
[1, 2, 3]
""")


