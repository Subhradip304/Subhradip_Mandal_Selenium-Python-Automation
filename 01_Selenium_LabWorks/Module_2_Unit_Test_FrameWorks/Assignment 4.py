import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    # Initialize Microsoft Edge Driver
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    yield driver
    driver.quit()


@pytest.mark.smoke
def test_name_field(driver):
    name_box = driver.find_element(By.ID, "name")
    name_box.clear()
    name_box.send_keys("Subhradip")

    assert name_box.get_attribute("value") == "Subhradip"

    print("Name field test passed for Subhradip")


@pytest.mark.smoke
def test_radio_button(driver):
    radio2 = driver.find_element(
        By.XPATH,
        "//input[@value='radio2']"
    )

    radio2.click()

    assert radio2.is_selected()

    print("Radio button test passed")


@pytest.mark.regression
def test_page_title(driver):
    assert driver.title.strip() != ""

    print(f"Page title test passed: '{driver.title}'")
