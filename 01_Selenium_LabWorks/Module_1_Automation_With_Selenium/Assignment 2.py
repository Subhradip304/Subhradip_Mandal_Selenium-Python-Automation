from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

wait = WebDriverWait(driver, 10)

# 1. Wait for the name field to become visible
name_box = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "name")
    )
)

name_box.send_keys("Harsh")

print("1. Explicit Wait: Name field is visible")

# 2. Wait for Radio2 to become clickable
radio2 = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@value='radio2']")
    )
)

radio2.click()

assert radio2.is_selected()

print("2. Explicit Wait: Radio2 is clickable and selected")

# 3. Wait for the dropdown to become visible
dropdown = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "dropdown-class-example")
    )
)

print("3. Explicit Wait: Dropdown is visible")

# 4. Wait for the Home link to become clickable
home_link = wait.until(
    EC.element_to_be_clickable(
        (By.LINK_TEXT, "Home")
    )
)

print("4. Explicit Wait: Home link is clickable")

# 5. Verify page URL
assert "rahulshettyacademy.com" in driver.current_url

print("5. URL verification successful")

print("\nAssignment 2 - Synchronization & Explicit Waits PASSED")

driver.quit()
