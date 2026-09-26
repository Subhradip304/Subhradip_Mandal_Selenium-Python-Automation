from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

wait = WebDriverWait(driver, 10)

# 1. WAIT FOR WEBTABLE
table = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//table")
    )
)

print("1. WebTable found")

# 2. FIND TABLE ROWS
rows = table.find_elements(
    By.XPATH,
    ".//tbody/tr"
)

print("2. Number of rows:", len(rows))

# 3. EXTRACT TABLE DATA
print("\nWebTable Data:")

for row_number, row in enumerate(rows, start=1):

    columns = row.find_elements(
        By.TAG_NAME,
        "td"
    )

    row_data = []

    for column in columns:
        row_data.append(column.text.strip())

    if row_data:
        print(f"Row {row_number}:", row_data)

# 4. VERIFY TABLE DATA
assert len(rows) > 0

print("\n3. Table contains data")

# 5. COUNT COLUMNS
first_data_row = None

for row in rows:
    columns = row.find_elements(
        By.TAG_NAME,
        "td"
    )

    if columns:
        first_data_row = columns
        break

if first_data_row:
    print("4. Number of columns:", len(first_data_row))

# 6. SEARCH FOR A VALUE
search_value = "Rahul"

found = False

for row in rows:

    columns = row.find_elements(
        By.TAG_NAME,
        "td"
    )

    for column in columns:

        if search_value.lower() in column.text.lower():
            found = True
            print(
                f"5. '{search_value}' found in table"
            )

            break

    if found:
        break

if not found:
    print(
        f"5. '{search_value}' was not found in the table"
    )

print("\nAssignment 5 - HTML WebTable Extractor PASSED")

driver.quit()
