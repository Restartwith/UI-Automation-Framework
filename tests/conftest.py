import os
import sys
from pathlib import Path
from datetime import datetime

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from utils.browser_factory import create_driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=os.getenv("BROWSER", "chrome"),
        help="Browser to run tests against: chrome or firefox",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode",
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    driver_instance = create_driver(browser_name=browser_name, headless=headless)
    driver_instance.maximize_window()

    yield driver_instance

    if request.node.rep_call.failed:
        screenshot_dir = ROOT / "screenshots"
        screenshot_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = screenshot_dir / f"{request.node.name}_{timestamp}.png"
        driver_instance.save_screenshot(str(screenshot_path))

    driver_instance.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
    return rep
