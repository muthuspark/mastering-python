import asyncio

async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(2) # await makes the coroutine pause
    print("Coroutine finished")


async def main():
    await my_coroutine()

asyncio.run(main())
