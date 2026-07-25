import time

from selenium.webdriver.common.by import By


class TestPlaceOrder:
    def test_PlaceOrder(self,Browser):
        Orderplacebtn = Browser.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/button")
        Orderplacebtn.click()
        time.sleep(6)