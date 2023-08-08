import asyncio

async def main():
    print("Abhi")
    task = asyncio.create_task(new())
    await asyncio.sleep(0)
    print("Finished")
    
async def new():
    print("Kittu")
    await asyncio.sleep(10)    

asyncio.run(main())