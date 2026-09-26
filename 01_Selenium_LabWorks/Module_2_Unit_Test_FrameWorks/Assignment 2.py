from selenium.webdriver.common.by import By


class TestSetupTeardown:

    def test_name(self, driver):
        name_box = driver.find_element(
            By.ID,
            "name"
        )

        name_box.send_keys("Harsh")

        assert name_box.get_attribute("value") == "Harsh"

        print("Name test passed")

    def test_radio(self, driver):
        radio = driver.find_element(
            By.XPATH,
            "//input[@value='radio2']"
        )

        radio.click()

        assert radio.is_selected()

        print("Radio test passed")

    def test_title(self, driver):
        assert driver.title.strip() != ""

        print("Title test passed")
