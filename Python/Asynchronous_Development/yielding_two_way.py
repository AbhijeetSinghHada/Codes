from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def get_friend():
    yield from friends


def greet(c):
    while True:
        try:
            friend = next(c)
            yield f'Hello {friend}'
        except StopIteration:
            pass


friends_generator = get_friend()
x = greet(friends_generator)

print(next(x))
print(next(x))
print(next(x))
