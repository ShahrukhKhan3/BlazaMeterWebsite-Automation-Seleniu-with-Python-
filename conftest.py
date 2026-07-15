import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def Browser():
        driver = webdriver.Firefox()
        driver.get("https://demoblaze.com/")
        yield driver
        driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("Browser", None)

        if driver:
            driver.save_screenshot(f"screenshots/{item.name}.png")