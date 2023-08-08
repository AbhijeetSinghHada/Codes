from Pages.quote_page import InvalidTagForAuthorError
from selenium import webdriver
from bs4 import BeautifulSoup
from Pages.quote_page import QuotesPage
try:
    author = input("Enter the Author You Want to Select : ")
    selected_tag = input("Enter your tag: ")
    chrome = webdriver.Chrome()
    chrome.get('https://quotes.toscrape.com/search.aspx')

    page = QuotesPage(chrome)

    print(page.search_for_quotes(author, selected_tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error occured")
