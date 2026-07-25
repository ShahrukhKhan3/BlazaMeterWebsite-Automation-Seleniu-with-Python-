import time

from selenium.webdriver.common.by import By


class TestClickProduct:
    time.sleep(7)
    def test_Click_Product(self,Browser):
        Prod=Browser.find_element(By.LINK_TEXT, "Samsung galaxy s6")
        Prod.click()
        time.sleep(5)