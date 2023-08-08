from Locators.book_locators import BookLocators
import re

Rating = {
    'One' : 1,
    'Two' : 2,
    'Three':3,
    'Four': 4,
    'Five':5
}

class BooksParser:
    def __init__(self,parent) -> None:
        self.parent=parent
        
    def __repr__(self) -> str:
        return f'<Book {self.content}, Price: {self.price}, Rating: {self.rating}>'
        
    @property
    def content(self):
        locator = BookLocators.NAME
        return self.parent.select_one(locator).attrs['title']
    
    @property
    def price(self):
        locator = BookLocators.PRICE
        item_link = self.parent.select_one(locator).string
        regex = '£[0-9]+\.[0-9]+'
        price = re.search(regex,item_link)
        price =price[0].replace('£','')
        return price
    
    @property
    def rating(self):
        locator = BookLocators.RATING
        rating_ext = self.parent.select_one(locator)
        rating  = rating_ext.attrs['class']
        rating = [i for i in rating if i!='star-rating']
        return Rating.get(rating[0])
    

        
