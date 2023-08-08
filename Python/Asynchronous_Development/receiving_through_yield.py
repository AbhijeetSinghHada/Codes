# def greet():
#     friend= yield
#     print(f'Hello, {friend}')

# g = greet()
# g.send(None)
# g.send("Abhi")
from collections import deque
friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield

        print(f'{greeting} {friend}')
    # yield from print(f'{greeting} {friend}')


def greet(g):
    # yield from g
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)


temp = friend_upper()
print(temp)
gr = greet(temp)
gr.send(None)
gr.send("Hello")
print("Hello, World MultiTasking...")
gr.send("Hiii")
