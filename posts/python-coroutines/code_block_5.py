import asyncio

async def my_async_context_manager():
    print("Entering context manager")
    try:
        yield "Resource"
    finally:
        print("Exiting context manager")

async def main():
    async with my_async_context_manager() as resource:
        print(f"Using resource: {resource}")

asyncio.run(main())
