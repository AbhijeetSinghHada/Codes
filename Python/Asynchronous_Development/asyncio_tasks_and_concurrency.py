import asyncio
import time


async def call_api(data):
    print("calling api with : ", data)
    await asyncio.sleep(data % 10)

    return data*100


async def pingger():
    for i in range(3):
        await asyncio.sleep(1)
        print("API is being called...")


async def main():

    start_time = time.perf_counter()


    # Tasks start running as soon as they get initialized
    task1 = asyncio.create_task(call_api(22))
    task2 = asyncio.create_task(call_api(33))


    await task1
    await task2

    # message_task = asyncio.create_task(pingger())

    # if we use normal sleep then program halts here for 3 sec then go further,
    # await asyncio.sleep(3)
    # taking total time 6 seconds

    # data1 = await task1
    # print(data1)

    # print("After task1 await")

    # data2 = await task2
    # print(data2)
    # print(task1.result())
    end = time.perf_counter()
    print(f"It took {start_time- end} seconds to complete.")

asyncio.run(main())
print("hello")
