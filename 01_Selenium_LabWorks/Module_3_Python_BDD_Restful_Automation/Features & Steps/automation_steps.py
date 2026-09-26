from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("the browser is opened")
def step_open_browser(context):
    # Initialize Microsoft Edge Driver
    context.driver = webdriver.Edge()
    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, 10)


@when("the user navigates to the Automation Practice page")
def step_open_page(context):
    context.driver.get(
        "https://rahulshettyacademy.com/AutomationPractice/"
    )


@then("the page title should be displayed")
def step_verify_page_title(context):
    assert context.driver.title.strip() != ""
    print("Page title verified:", context.driver.title)


@when('the user enters name "{name}"')
def step_enter_name(context, name):
    name_box = context.wait.until(
        EC.visibility_of_element_located((By.ID, "name"))
    )
    name_box.clear()
    name_box.send_keys(name)

    assert name_box.get_attribute("value") == name
    print(f"Name entered successfully: {name}")


@then("the name should be entered successfully")
def step_verify_name(context):
    name_box = context.driver.find_element(By.ID, "name")
    assert name_box.get_attribute("value") == "Subhradip"
    print(f"Name verified as Subhradip: {name_box.get_attribute('value')}")


@when("the user selects Radio2")
def step_select_radio2(context):
    radio2 = context.wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@value='radio2']")
        )
    )
    radio2.click()


@then("Radio2 should be selected")
def step_verify_radio2(context):
    radio2 = context.driver.find_element(
        By.XPATH, "//input[@value='radio2']"
    )
    assert radio2.is_selected()
    print("Radio2 selected successfully by Subhradip")


@when("the user clicks the Alert button")
def step_click_alert(context):
    alert_button = context.wait.until(
        EC.element_to_be_clickable((By.ID, "alertbtn"))
    )
    alert_button.click()


@then("the alert should be displayed")
def step_verify_alert(context):
    alert = context.wait.until(
        EC.alert_is_present()
    )

    assert alert is not None
    assert "Subhradip" in alert.text

    print("Alert text verified for Subhradip:", alert.text)

    alert.accept()


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
