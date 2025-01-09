import asyncio

async def my_io_bound_task(delay):
    print(f"Task started: {delay}")
    await asyncio.sleep(delay) # Simulates an I/O operation
    print(f"Task finished: {delay}")
    return delay * 2

async def main():
    task1 = asyncio.create_task(my_io_bound_task(2))
    task2 = asyncio.create_task(my_io_bound_task(1))
    task3 = asyncio.create_task(my_io_bound_task(3))

    results = await asyncio.gather(task1, task2, task3)
    print(f"Results: {results}")

if __name__ == "__main__":
    asyncio.run(main())