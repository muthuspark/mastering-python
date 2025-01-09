import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ["https://www.example.com", "https://www.google.com", "https://www.python.org"]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for i, result in enumerate(results):
            print(f"URL {urls[i]}: {len(result)} characters")


asyncio.run(main())