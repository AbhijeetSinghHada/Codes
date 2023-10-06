import asyncio


async def new():
    print("Kittu")
    await asyncio.sleep(2)
    print("after 10 Sleep")


async def main():
    print("Abhi")
    task = asyncio.create_task(new())
    task2 = asyncio.create_task(new())
    # await asyncio.sleep(0)
    # print(asyncio.current_task())
    # print(asyncio.all_tasks()) all tasks that are pending to be completed or under the event loop execution

    # await task  # These are needed for new() to first complete its whole processing otherwise
    # await task2 #lines of code after await doent run
    print("Finished")


asyncio.run(main())
