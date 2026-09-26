import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize(
    "name",
    ["Harsh", "Rahul", "Selenium"]
)
def test_enter_multiple_names(driver, name):

    name_box = driver.find_element(
        By.ID,
        "name"
    )

    name_box.send_keys(name)

    assert name_box.get_attribute("value") == name

    print("Name entered:", name)
