from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from typing import List
from selenium.webdriver.support.select import Select
from Locators.quote_page_locators import QuotesPageLocator
from Parsers.qutoes import QuoteParser
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class QuotesPage:
    def __init__(self, browser) -> None:
        self.browser = browser

    @property
    def quotes(self):
        locators = QuotesPageLocator.QUOTE
        return [QuoteParser(e) for e in self.browser.find_elements(By.CSS_SELECTOR, locators)]

    @property
    def author_dropdown(self) -> Select:
        locators = QuotesPageLocator.AUTHOR_DROPDOWN
        element = self.browser.find_element(By.CSS_SELECTOR, locators)
        return Select(element)

    @property
    def tag_dropdown(self) -> Select:
        locators = QuotesPageLocator.TAG_DROPDOWN
        element = self.browser.find_element(By.CSS_SELECTOR, locators)
        return Select(element)

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def select_tag(self, tag_name: str):
        self.tag_dropdown.select_by_visible_text(tag_name)

    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tag_dropdown.options]

    @property
    def search_button(self):
        locators = QuotesPageLocator.SEARCH_BUTTON
        return self.browser.find_element(By.CSS_SELECTOR, locators)

    def search_for_quotes(self, author_name: str, tag_name: str) -> List[QuoteParser]:
        self.select_author(author_name)
        # time.sleep(5) beter use wait until
        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, QuotesPageLocator.TAG_DROPDOWN_VALUE_OPTION)
            ))
        try:
            self.select_tag(tag_name)
        except NoSuchElementException:
            raise InvalidTagForAuthorError(
                f"Author '{author_name}' does not have any quote tagged with '{tag_name}'"
            )
        self.search_button.click()
        return self.quotes


class InvalidTagForAuthorError(ValueError):
    pass
