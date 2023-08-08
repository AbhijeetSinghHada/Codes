from bs4 import BeautifulSoup
from Locators.book_page_locators import BooksPageLocator
from Parsers.Books import BooksParser

class BooksPage:
    def __init__(self,page) -> None:
        self.soup = BeautifulSoup(page,'html.parser')
         
    @property
    def books(self):
        locators = BooksPageLocator.BOOK
        book_tags = self.soup.select(locators)
        return [BooksParser(e) for e in book_tags]