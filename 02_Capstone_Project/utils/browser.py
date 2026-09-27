"""WebDriver factory."""

from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def create_driver(browser: str, headless: bool):

    if browser == "edge":
        options = EdgeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Edge(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()

        if headless:
            options.add_argument("-headless")

        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(
            f"Unsupported browser: {browser}. Use edge or firefox."
        )

    if not headless:
        driver.maximize_window()

    return driver