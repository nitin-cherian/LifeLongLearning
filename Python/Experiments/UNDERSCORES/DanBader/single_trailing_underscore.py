# single_trailing_underscore.py

print("""
1. Sometimes the most apt name for a variable or method is already taken by a keyword(class, def etc).
2. Use trailing underscore to avoid the name conflict.
3. Used by convention to avoid name conflict.

def make_object(name, class):
    pass
    
# SyntaxError: invalid syntax
    
def make_another_object(name, class_)
    pass
""")

# def make_object(name, class):
#     pass

def make_another_object(name, class_):
    pass


