import time

from _pytest import unittest
from selenium.webdriver.common.by import By


class TestAddToCart:
    def test_AddTocart(self,Browser):
        Addtocartbtn = Browser.find_element(By.LINK_TEXT, "Add to cart")
        Addtocartbtn.click()
        time.sleep(6)
    def test_Dialogue(self, Browser):
        alert = Browser.switch_to.alert
        print(alert.text)
        alert.accept()