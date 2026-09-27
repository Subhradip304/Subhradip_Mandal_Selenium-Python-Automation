# Page object for the store home page: opens the site, navigates to login, and searches products.
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")
    MY_ACCOUNT = (By.LINK_TEXT, "My Account")
    LOGIN = (By.LINK_TEXT, "Login")

    def open(self, url: str):
        self.driver.get(url)

    def go_to_login(self):
        self.click(self.MY_ACCOUNT)
        self.click(self.LOGIN)

    def search(self, product: str):
        self.type(self.SEARCH, product)
        self.click(self.SEARCH_BUTTON)
