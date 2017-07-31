# decorator.py


def info(func):
    def wrapper(*args):
        print('Function name: ', func.__name__)
        print('Function docs: ', func.__doc__)
        return func(*args)
    return wrapper


@info
def doubler(number):
    """ Doubles the number that is passed as argument """
    return number * 2

print(doubler(2))

