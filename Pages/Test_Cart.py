import time

from selenium.webdriver.common.by import By


class TestCart:
    def test_Cart(self, Browser):
        Addtocartmenulink = Browser.find_element(By.ID, "cartur")
        Addtocartmenulink.click()
        time.sleep(5)