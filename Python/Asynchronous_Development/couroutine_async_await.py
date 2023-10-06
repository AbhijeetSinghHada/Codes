import asyncio


friends = ['Bob', 'Rolf', 'Anne']


def my_func():
    print("Hello")
    while True:
        friend = (yield)
        print(friend)


async def corrutine(hello):
    hello.send(None)
    while True:
        friend = await hello.send(friends[0])
        friends.pop(0)
        print(friend)


async def main():
    hello = my_func()

    task = asyncio.create_task(corrutine(hello))
    await task

asyncio.run(main())
