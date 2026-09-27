# Loads environment variables and exposes immutable settings used by the test run.
"""Environment-backed execution settings."""
from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "https://tutorialsninja.com/demo/")
    browser: str = os.getenv("BROWSER", "chrome").lower()
    headless: bool = os.getenv("HEADLESS", "false").lower() == "true"
    timeout: int = int(os.getenv("TIMEOUT", "15"))
    action_delay: float = float(os.getenv("ACTION_DELAY", "1.5"))
    email: str = os.getenv("DEMO_EMAIL", "")
    password: str = os.getenv("DEMO_PASSWORD", "")


settings = Settings()
