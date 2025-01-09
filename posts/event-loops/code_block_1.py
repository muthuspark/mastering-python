import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = "https://www.example.com"
    page_content = await fetch_url(url)
    print(f"Page content length: {len(page_content)}")

asyncio.run(main())