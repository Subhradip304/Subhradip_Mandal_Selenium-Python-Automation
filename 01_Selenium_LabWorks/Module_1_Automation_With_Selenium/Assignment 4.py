from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Microsoft Edge Driver
driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

wait = WebDriverWait(driver, 10)

# 1. ENTER NAME
name_box = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "name")
    )
)

name_box.send_keys("Subhradip")

print("1. Name entered as Subhradip")

# 2. JAVASCRIPT ALERT
alert_button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "alertbtn")
    )
)

alert_button.click()

# Wait for alert to appear
wait.until(
    EC.alert_is_present()
)

alert = driver.switch_to.alert

print("2. Alert text:", alert.text)

assert "Hello Subhradip" in alert.text

alert.accept()

print("3. Alert accepted")

# 3. JAVASCRIPT CONFIRM
# Re-enter name for confirm box verification
name_box = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "name")
    )
)
name_box.send_keys("Subhradip")

confirm_button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "confirmbtn")
    )
)

confirm_button.click()

# Wait for confirm alert
wait.until(
    EC.alert_is_present()
)

confirm = driver.switch_to.alert

print("4. Confirm text:", confirm.text)

assert "Hello Subhradip" in confirm.text

# Accept the confirm
confirm.accept()

print("5. Confirm accepted")

# 4. TEST CONFIRM DISMISS
confirm_button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "confirmbtn")
    )
)

confirm_button.click()

# Wait for confirm alert
wait.until(
    EC.alert_is_present()
)

confirm = driver.switch_to.alert

print("6. Second confirm displayed")

# Dismiss the confirm
confirm.dismiss()

print("7. Confirm dismissed")

print("\nAssignment 4 - JavaScript Alerts & Confirms PASSED by Subhradip")

driver.quit()
