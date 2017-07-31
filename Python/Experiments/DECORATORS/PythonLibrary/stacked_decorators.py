# stacked_decorators.py


def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper


def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper


@italic
@bold
def formatted_text():
    return 'Python Rocks!'


print(formatted_text())
