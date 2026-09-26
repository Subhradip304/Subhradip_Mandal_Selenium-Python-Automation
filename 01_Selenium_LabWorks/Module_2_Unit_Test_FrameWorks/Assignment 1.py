from selenium.webdriver.common.by import By


class TestAutomationPractice:

    def test_enter_name(self, driver):
        name_box = driver.find_element(
            By.ID,
            "name"
        )

        name_box.send_keys("Harsh")

        assert name_box.get_attribute("value") == "Harsh"

        print("Name entered successfully")

    def test_radio_button(self, driver):
        radio2 = driver.find_element(
            By.XPATH,
            "//input[@value='radio2']"
        )

        radio2.click()

        assert radio2.is_selected()

        print("Radio2 selected successfully")

    def test_page_title(self, driver):
        assert driver.title.strip() != ""

        print("Page title verified")
