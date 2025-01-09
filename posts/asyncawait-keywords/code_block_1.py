import asyncio

async def potentially_failing_task():
    try:
        # Some operation that might raise an exception
        await asyncio.sleep(1)  # Simulate some work
        raise Exception("Something went wrong!")
    except Exception as e:
        print(f"An error occurred: {e}")

async def main():
    await potentially_failing_task()

if __name__ == "__main__":
    asyncio.run(main())