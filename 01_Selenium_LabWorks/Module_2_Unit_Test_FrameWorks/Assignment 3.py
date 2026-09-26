import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def driver():
    # Initialize Microsoft Edge Driver
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "name",
    ["Subhradip", "Rahul", "Selenium"]
)
def test_enter_multiple_names(driver, name):

    name_box = driver.find_element(
        By.ID,
        "name"
    )

    name_box.clear()
    name_box.send_keys(name)

    assert name_box.get_attribute("value") == name

    print(f"Name entered successfully: {name}")
