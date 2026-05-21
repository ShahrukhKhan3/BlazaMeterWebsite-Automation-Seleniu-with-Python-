from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait


class DriverSetup:

    @staticmethod
    def get_driver():

        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://demoblaze.com/")

        wait = WebDriverWait(driver, 10)

        return driver, wait