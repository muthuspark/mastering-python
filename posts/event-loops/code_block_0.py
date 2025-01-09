import asyncio

async def my_task(name):
    print(f"Task {name}: Starting")
    await asyncio.sleep(1)  # Simulate I/O operation
    print(f"Task {name}: Finishing")

async def main():
    task1 = asyncio.create_task(my_task("A"))
    task2 = asyncio.create_task(my_task("B"))
    await task1
    await task2

asyncio.run(main())