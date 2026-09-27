# Defines shared pytest setup: browser lifecycle, failure screenshots, and test-result hooks.
import pytest

from utils.browser import create_driver
from utils.config import settings
from utils.helpers import capture_screenshot, clear_previous_screenshots


@pytest.fixture(scope="session", autouse=True)
def clean_screenshot_folder():
    """Start every execution with an empty screenshot output folder."""
    clear_previous_screenshots()


@pytest.fixture
def driver(request):
    web_driver = create_driver(settings.browser, settings.headless)
    web_driver.implicitly_wait(0)
    yield web_driver
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        capture_screenshot(web_driver, f"FAILED_{request.node.name}")
    web_driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
