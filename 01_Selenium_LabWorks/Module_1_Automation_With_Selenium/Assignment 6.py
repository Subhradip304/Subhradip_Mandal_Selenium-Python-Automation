from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Microsoft Edge Driver
driver = webdriver.Edge()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Brand session with tester name
try:
    name_box = wait.until(
        EC.visibility_of_element_located((By.ID, "name"))
    )
    name_box.send_keys("Subhradip")
    print("Tester Name entered: Subhradip")
except Exception:
    pass

# 1. STORE MAIN WINDOW
main_window = driver.current_window_handle

print("1. Main window stored")

# 2. WAIT FOR OPEN TAB LINK
open_tab = wait.until(
    EC.element_to_be_clickable(
        (By.LINK_TEXT, "Open Tab")
    )
)

open_tab.click()

print("2. Open Tab clicked")

# 3. WAIT FOR NEW WINDOW/TAB
wait.until(
    EC.number_of_windows_to_be(2)
)

print("3. New tab opened")

# 4. SWITCH TO NEW TAB
for window in driver.window_handles:

    if window != main_window:
        driver.switch_to.window(window)
        break

print("4. Switched to new tab")

# 5. VERIFY NEW TAB
print("New tab URL:", driver.current_url)
print("New tab title:", driver.title)

assert driver.current_window_handle != main_window

print("5. New tab verified")

# 6. CLOSE NEW TAB
driver.close()

print("6. New tab closed")

# 7. SWITCH BACK TO MAIN WINDOW
driver.switch_to.window(main_window)

print("7. Switched back to main window")

assert driver.current_window_handle == main_window

# 8. VERIFY MAIN PAGE
print("Main page URL:", driver.current_url)

assert "rahulshettyacademy.com" in driver.current_url

print("8. Main page verified")

# 9. IFRAME
iframe = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//iframe")
    )
)

print("9. Iframe found")

# 10. SWITCH INTO IFRAME
driver.switch_to.frame(iframe)

print("10. Switched into iframe")

# 11. VERIFY IFRAME CONTENT
iframe_body = wait.until(
    EC.presence_of_element_located(
        (By.TAG_NAME, "body")
    )
)

print("Iframe content loaded")
print("Iframe text preview:", iframe_body.text[:100])

# 12. SWITCH BACK TO MAIN PAGE
driver.switch_to.default_content()

print("11. Switched back to main page")

# 13. FINAL VERIFICATION
assert driver.current_window_handle == main_window

print("\nAssignment 6 - Windows, Tabs & Iframes PASSED by Subhradip")

driver.quit()
