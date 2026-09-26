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


class TestSetupTeardown:

    def test_name(self, driver):
        name_box = driver.find_element(
            By.ID,
            "name"
        )

        name_box.clear()
        name_box.send_keys("Subhradip")

        assert name_box.get_attribute("value") == "Subhradip"

        print("Name test passed for Subhradip")

    def test_radio(self, driver):
        radio = driver.find_element(
            By.XPATH,
            "//input[@value='radio2']"
        )

        radio.click()

        assert radio.is_selected()

        print("Radio test passed")

    def test_title(self, driver):
        assert driver.title.strip() != ""

        print(f"Title test passed: '{driver.title}'")
