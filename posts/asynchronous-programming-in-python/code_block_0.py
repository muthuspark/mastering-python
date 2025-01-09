import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        urls = ["https://www.example.com", "https://www.python.org", "https://www.google.com"]
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for url, result in zip(urls, results):
            print(f"Content from {url}: {result[:100]}...") #Print first 100 characters

if __name__ == "__main__":
    asyncio.run(main())