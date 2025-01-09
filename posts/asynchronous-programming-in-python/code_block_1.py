import asyncio

async def might_fail(delay):
    await asyncio.sleep(delay)
    if delay > 2:
        raise Exception("Something went wrong!")
    return f"Success after {delay} seconds!"

async def main():
    tasks = [might_fail(i) for i in range(4)]
    results = []
    for task in asyncio.as_completed(tasks):
        try:
            result = await task
            results.append(result)
        except Exception as e:
            print(f"An error occurred: {e}")
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
