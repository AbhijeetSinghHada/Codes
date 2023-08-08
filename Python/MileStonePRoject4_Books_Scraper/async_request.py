import aiohttp
import asyncio
import async_timeout
import time


async def fetch_page(session, url):
    page_state = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f'Page Took : {time.time() - page_state}')
            return await response


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


loop = asyncio.get_event_loop()

page_state = time.time()
urls = [
    f'http://books.toscrape.com/catalogue/page-{i}.html' for i in range(1, 51)]
data = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'AsyncIO Took : {time.time() - page_state}\n\n')

for d in data:
    print(d)
