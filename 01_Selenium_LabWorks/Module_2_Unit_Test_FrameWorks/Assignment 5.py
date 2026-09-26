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


def test_enter_name(driver):
    name_box = driver.find_element(
        By.ID,
        "name"
    )

    name_box.clear()
    name_box.send_keys("Subhradip")

    assert name_box.get_attribute("value") == "Subhradip"

    print("Name entered successfully as Subhradip")


def test_radio_button(driver):
    radio2 = driver.find_element(
        By.XPATH,
        "//input[@value='radio2']"
    )

    radio2.click()

    assert radio2.is_selected()

    print("Radio2 selected successfully")


def test_checkbox(driver):
    checkbox = driver.find_element(
        By.ID,
        "checkBoxOption1"
    )

    checkbox.click()

    assert checkbox.is_selected()

    print("Checkbox selected successfully")
