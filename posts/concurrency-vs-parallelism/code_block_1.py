import asyncio

async def task(name, delay):
    print(f"Task {name}: starting")
    await asyncio.sleep(delay)
    print(f"Task {name}: finishing")

async def main():
    tasks = [task(i, 1) for i in range(3)] # Each task sleeps for 1 second.
    await asyncio.gather(*tasks) # Run all tasks concurrently.

    print("All tasks completed.")


asyncio.run(main())