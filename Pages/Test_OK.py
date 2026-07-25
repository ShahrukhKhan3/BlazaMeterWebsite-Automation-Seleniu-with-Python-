import time

from selenium.webdriver.common.by import By


class TestOK:
    def test_OK(self,Browser):
     ok_btn = Browser.find_element(By.XPATH, "//button[text()='OK']")
     time.sleep(1)
     ok_btn.click()