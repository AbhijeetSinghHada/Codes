import aiohttp
import asyncio
import async_timeout
import time
from Pages.book_page import BooksPage
import logging
import requests

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s: %(lineno)d]: %(message)s',
                    level=logging.DEBUG,
                    datefmt='%d-%m-%Y %H:%M:%S',
                    filename='logs.txt')
logger = logging.getLogger('scraping')
loop = asyncio.get_event_loop()

logger.info('Loading Book List...')

page_content = requests.get(f'http://books.toscrape.com').content
page = BooksPage(page_content)
books = page.books


async def fetch_page(session, url):
    page_state = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f'Page Took : {time.time() - page_state}')
            return await response.text()


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

urls = [
    f'http://books.toscrape.com/catalogue/page-{i}.html' for i in range(1, 51)]
page_start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))

print(f'AsyncIO Took : {time.time() - page_start}\n\n')


books = []
for page_content in pages:
    page = BooksPage(page_content)
    books.extend(page.books)
