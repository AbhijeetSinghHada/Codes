from bs4 import BeautifulSoup
from Locators.quote_page_locators import QuotesPageLocator
from Parsers.qutoes import QuoteParser

class QuotesPage:
    def __init__(self,page) -> None:
        self.soup = BeautifulSoup(page,'html.parser')
        
    @property
    def quotes(self):
        locators = QuotesPageLocator.QUOTE
        quote_tags = self.soup.select(locators)
        return [QuoteParser(e) for e in quote_tags]