import asyncio

async def worker1(event):
    print("Worker 1 starting")
    await asyncio.sleep(2)
    print("Worker 1 finishing")
    event.set() # Signal completion

async def worker2(event):
    print("Worker 2 starting")
    await event.wait()  # Wait for the signal
    print("Worker 2 finishing")

async def main():
    event = asyncio.Event()
    await asyncio.gather(worker1(event), worker2(event))

if __name__ == "__main__":
    asyncio.run(main())