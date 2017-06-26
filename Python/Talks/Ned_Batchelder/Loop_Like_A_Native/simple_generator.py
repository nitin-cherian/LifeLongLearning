# simple_generator.py


def hello_world():
    yield "hello"
    yield "world"


for word in hello_world():
    print(word)
