# Shared Selenium actions used by every page object, including safe waits, clicks, and text entry.
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import settings


class BasePage:
    def __init__(self, driver, timeout: int):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()
        self._pause()

    def type(self, locator, value: str):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        for character in value:
            element.send_keys(character)
            time.sleep(0.08)
        self._pause()

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @staticmethod
    def _pause():
        """Add a visible gap between actions when the test is presented live."""
        time.sleep(settings.action_delay)
