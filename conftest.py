import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def Browser():
        driver = webdriver.Firefox()
        driver.get("https://demoblaze.com/")
        yield driver
        driver.quit()