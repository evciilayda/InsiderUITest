import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime

def pytest_addoption(parser):
    parser.addoption(
        "--driver", action="store", default="chrome", help="Choose the browser: chrome or firefox"
    )

@pytest.fixture
def driver(request):
    browser = request.config.getoption("driver")
    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Geçersiz tarayıcı: {browser}")

    driver.get("https://useinsider.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver', None)
        if driver:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{screenshot_dir}/{item.name}_{timestamp}.png"
            driver.save_screenshot(file_name)
            print(f"Ekran görüntüsü alındı: {file_name}")
