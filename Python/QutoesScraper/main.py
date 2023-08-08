import requests
from bs4 import BeautifulSoup
from Pages.quote_page import QuotesPage

page_content  = requests.get('http://quotes.toscrape.com').content

page = QuotesPage(page_content)

for quote in page.quotes:
    print(quote.content," By ",quote.author)