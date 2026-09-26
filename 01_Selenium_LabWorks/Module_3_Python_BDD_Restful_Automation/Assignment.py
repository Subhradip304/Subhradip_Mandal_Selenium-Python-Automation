from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

assert driver.title.strip() != ""
print("Page title test passed")

name_field = wait.until(
    EC.visibility_of_element_located((By.ID, "name"))
)

name_field.clear()
name_field.send_keys("Harsh")

assert name_field.get_attribute("value") == "Harsh"
print("Name field test passed")

radio2 = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@value='radio2']")
    )
)

radio2.click()

assert radio2.is_selected()
print("Radio2 test passed")

alert_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@value='Alert']")
    )
)

alert_button.click()

alert = wait.until(
    EC.alert_is_present()
)

print("Alert text:", alert.text)

assert alert is not None

alert.accept()

print("Alert test passed")
print("All Selenium tests passed")

driver.quit()
