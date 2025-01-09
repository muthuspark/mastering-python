import asyncio

async def fetch_data(url):
    # Simulate network request
    await asyncio.sleep(1)  # Simulate I/O wait
    print(f"Fetched data from {url}")
    return f"Data from {url}"

async def main():
    tasks = [fetch_data("url1"), fetch_data("url2"), fetch_data("url3")]
    results = await asyncio.gather(*tasks)
    print(f"Results: {results}")

asyncio.run(main())