from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

wait = WebDriverWait(driver, 10)

# 1. DYNAMIC DROPDOWN
country = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "autocomplete")
    )
)

country.send_keys("Ind")

print("1. Dynamic dropdown: 'Ind' entered")

# Wait for the suggestions to appear
suggestions = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".ui-menu-item")
    )
)

print("2. Suggestions found:", len(suggestions))

# Select India from the suggestions
india_found = False

for suggestion in suggestions:
    if suggestion.text.strip() == "India":
        suggestion.click()
        india_found = True
        break

assert india_found

print("3. Dynamic dropdown: India selected")

# 2. CHECKBOXES
checkboxes = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "input[type='checkbox']")
    )
)

print("4. Checkboxes found:", len(checkboxes))

# Select the first checkbox
first_checkbox = checkboxes[0]

if not first_checkbox.is_selected():
    first_checkbox.click()

assert first_checkbox.is_selected()

print("5. First checkbox selected")

# Select the second checkbox
if len(checkboxes) > 1:
    second_checkbox = checkboxes[1]

    if not second_checkbox.is_selected():
        second_checkbox.click()

    assert second_checkbox.is_selected()

    print("6. Second checkbox selected")

print("\nAssignment 3 - Dynamic Dropdowns & Checkboxes PASSED")

driver.quit()
