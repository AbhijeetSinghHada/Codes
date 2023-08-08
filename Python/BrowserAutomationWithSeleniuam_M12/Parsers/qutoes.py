from Locators.quote_locators import QuoteLocators
from selenium.webdriver.common.by import By
class QuoteParser:
    def __init__(self,parent) -> None:
        self.parent=parent
        
    def __repr__(self) -> str:
        return f'<Quote {self.content}, by {self.author}>'
        
    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.find_element(By.CSS_SELECTOR,locator).text
    
    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.find_element(By.CSS_SELECTOR, locator).text
    
    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return self.parent.find_element(By.CSS_SELECTOR, locator)

        
