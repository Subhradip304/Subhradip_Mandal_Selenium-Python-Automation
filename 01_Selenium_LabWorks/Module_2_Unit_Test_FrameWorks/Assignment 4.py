import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    yield driver
    driver.quit()


@pytest.mark.smoke
def test_name_field(driver):
    name_box = driver.find_element(By.ID, "name")
    name_box.send_keys("Harsh")

    assert name_box.get_attribute("value") == "Harsh"

    print("Name field test passed")


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

    print("Page title test passed")
