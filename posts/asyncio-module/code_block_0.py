import asyncio

async def my_coroutine(delay):
    print(f"Coroutine started with delay: {delay}")
    await asyncio.sleep(delay)
    print(f"Coroutine finished after {delay} seconds")
    return delay * 2

async def main():
    task1 = asyncio.create_task(my_coroutine(1))
    task2 = asyncio.create_task(my_coroutine(2))
    results = await asyncio.gather(task1, task2)
    print(f"Results: {results}")

asyncio.run(main())