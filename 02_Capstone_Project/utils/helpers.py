# Provides reusable screenshot capture and optional JavaScript alert handling.
from datetime import datetime
from pathlib import Path

from selenium.common.exceptions import NoAlertPresentException

ROOT = Path(__file__).resolve().parents[1]
SCREENSHOTS = ROOT / "screenshots"


def clear_previous_screenshots() -> None:
    """Remove screenshots from an earlier execution before a new test session starts."""
    SCREENSHOTS.mkdir(exist_ok=True)
    for screenshot in SCREENSHOTS.glob("*.png"):
        screenshot.unlink()


def capture_screenshot(driver, label: str) -> Path:
    SCREENSHOTS.mkdir(exist_ok=True)
    safe_label = "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in label)
    path = SCREENSHOTS / f"{datetime.now():%Y%m%d_%H%M%S}_{safe_label}.png"
    driver.save_screenshot(str(path))
    return path


def accept_alert_if_present(driver) -> bool:
    """Accept an unexpected JavaScript alert without failing when none exists."""
    try:
        driver.switch_to.alert.accept()
        return True
    except NoAlertPresentException:
        return False
