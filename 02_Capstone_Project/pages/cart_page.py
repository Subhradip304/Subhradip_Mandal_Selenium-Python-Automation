# Page object for updating cart quantities and reading product, price, and total details for verification.
from decimal import Decimal

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    QUANTITY = (By.CSS_SELECTOR, "input[name^='quantity']")
    UPDATE = (By.CSS_SELECTOR, "button[data-original-title='Update']")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".table-bordered tbody tr td:nth-child(2) a")
    UNIT_PRICE = (By.CSS_SELECTOR, ".table-bordered tbody tr td:nth-child(5)")
    LINE_TOTAL = (By.CSS_SELECTOR, ".table-bordered tbody tr td:nth-child(6)")

    def update_quantity(self, quantity: int):
        self.type(self.QUANTITY, str(quantity))
        self.click(self.UPDATE)

    def details(self) -> dict:
        return {
            "name": self.visible(self.PRODUCT_NAME).text,
            "quantity": int(self.visible(self.QUANTITY).get_attribute("value")),
            "unit_price": self._money(self.visible(self.UNIT_PRICE).text),
            "line_total": self._money(self.visible(self.LINE_TOTAL).text),
        }

    @staticmethod
    def _money(value: str) -> Decimal:
        return Decimal("".join(ch for ch in value if ch.isdigit() or ch == "."))
