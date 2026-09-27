# Page object for entering customer credentials and confirming a successful login.
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='Login']")
    ACCOUNT_BREADCRUMB = (By.LINK_TEXT, "Account")

    def login(self, email: str, password: str):
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        self.visible(self.ACCOUNT_BREADCRUMB)
