# Page object for search results: adds the first matching product and opens the shopping cart.
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):
    ADD_TO_CART = (By.CSS_SELECTOR, ".product-layout:first-of-type button[onclick*='cart.add']")
    SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    CART_TOTAL = (By.ID, "cart-total")

    def add_first_result_to_cart(self):
        self.click(self.ADD_TO_CART)
        self.visible(self.SUCCESS)

    def open_cart(self):
        self.click(self.CART_TOTAL)
        self.click((By.LINK_TEXT, "View Cart"))
