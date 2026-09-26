from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Microsoft Edge Driver
driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# 1. BY.ID
name_box = driver.find_element(
    By.ID,
    "name"
)

name_box.send_keys("Subhradip")

print("1. By.ID: Name entered as Subhradip")

# 2. BY.XPATH
radio2 = driver.find_element(
    By.XPATH,
    "//input[@value='radio2']"
)

radio2.click()

assert radio2.is_selected()

print("2. By.XPATH: Radio2 selected")

# 3. BY.CSS_SELECTOR
radio1 = driver.find_element(
    By.CSS_SELECTOR,
    "input[value='radio1']"
)

radio1.click()

assert radio1.is_selected()

print("3. By.CSS_SELECTOR: Radio1 selected")

# 4. BY.NAME
checkboxes = driver.find_elements(
    By.NAME,
    "checkBoxOption"
)

print("4. By.NAME: Elements found:", len(checkboxes))

# 5. BY.TAG_NAME
links = driver.find_elements(
    By.TAG_NAME,
    "a"
)

print("5. By.TAG_NAME: Number of links:", len(links))

# 6. BY.CLASS_NAME
element = driver.find_element(
    By.CLASS_NAME,
    "inputs"
)

print("6. By.CLASS_NAME: Element found")

# 7. BY.LINK_TEXT
home_link = driver.find_element(
    By.LINK_TEXT,
    "Home"
)

print("7. By.LINK_TEXT: Home link found")

# 8. BY.PARTIAL_LINK_TEXT
open_tab_link = driver.find_element(
    By.PARTIAL_LINK_TEXT,
    "Open"
)

print("8. By.PARTIAL_LINK_TEXT: Open Tab link found")

# 9. PAGE TITLE
print("Page title:", driver.title)

assert driver.title.strip() != ""

print("9. Page title verified")

print("\nMulti-Locator Challenge PASSED by Subhradip")

driver.quit()
