import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    # Initialize Microsoft Edge Driver
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    yield driver
    driver.quit()


@pytest.mark.smoke
def test_name_field(driver):
    name_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "name")
        )
    )

    name_box.clear()
    name_box.send_keys("Subhradip")

    assert name_box.get_attribute("value") == "Subhradip"

    print("Name field test passed for Subhradip")


@pytest.mark.smoke
def test_radio_button(driver):
    radio2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@value='radio2']")
        )
    )

    radio2.click()

    assert radio2.is_selected()

    print("Radio button test passed")


@pytest.mark.regression
def test_checkbox(driver):
    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "checkBoxOption1")
        )
    )

    checkbox.click()

    assert checkbox.is_selected()

    print("Checkbox test passed")


@pytest.mark.parametrize(
    "name",
    ["Subhradip", "Rahul", "Selenium"]
)
def test_multiple_names(driver, name):
    name_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "name")
        )
    )

    name_box.clear()
    name_box.send_keys(name)

    assert name_box.get_attribute("value") == name

    print("Name entered:", name)
