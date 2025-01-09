import asyncio

async def potentially_failing_coroutine():
    try:
        # Simulate an error
        result = 1 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError in coroutine")
        return "Error handled"
    return result

async def main():
  result = await potentially_failing_coroutine()
  print(f"Result: {result}")

asyncio.run(main())