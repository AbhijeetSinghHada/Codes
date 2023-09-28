# i = 1


# def greet():
#     global i
#     i += 1
#     yield f"Hello, Boy{i}"


# print(next(greet()))
# print(i)

# print(next(greet()))
# print(i)

from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    yield from g


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
print('Hello, world! Multitasking...')
greeter.send('How are you,')
