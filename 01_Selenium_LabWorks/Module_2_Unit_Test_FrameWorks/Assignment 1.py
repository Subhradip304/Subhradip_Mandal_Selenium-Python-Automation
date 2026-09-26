import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def driver():
    # Initialize Microsoft Edge Driver
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    yield driver
    driver.quit()


class TestAutomationPractice:

    def test_enter_name(self, driver):
        name_box = driver.find_element(
            By.ID,
            "name"
        )

        name_box.clear()
        name_box.send_keys("Subhradip")

        assert name_box.get_attribute("value") == "Subhradip"

        print("Name 'Subhradip' entered successfully")

    def test_radio_button(self, driver):
        radio2 = driver.find_element(
            By.XPATH,
            "//input[@value='radio2']"
        )

        radio2.click()

        assert radio2.is_selected()

        print("Radio2 selected successfully by Subhradip")

    def test_page_title(self, driver):
        assert driver.title.strip() != ""

        print(f"Page title verified: '{driver.title}'")
