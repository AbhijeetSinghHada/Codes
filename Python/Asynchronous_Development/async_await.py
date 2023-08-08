from types import coroutine
from collections import deque
friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield

        print(f'{greeting} {friend}')
    # yield from print(f'{greeting} {friend}')


async def greet(g):
    print("Starting...")
    await g
    print("Stoping...")


temp = friend_upper()
print(temp)
gr = greet(temp)
print(gr)
gr.send(None)
gr.send("Hello")
print("Hello, World MultiTasking...")
gr.send("Hiii")
gr.send("Hello")
print("Hello, World MultiTasking...")
gr.send("Hiii")
gr.send("Hello")
gr.send("Hello")
