import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

class TestSignup:
    def test_click_signup(self, Browser):
        Browser.find_element(By.ID, "signin2").click()
        time.sleep(4)
        Browser.find_element(By.ID, "sign-username").send_keys("Shahrukh")
        Browser.find_element(By.ID, "sign-password").send_keys("12345")
        Browser.find_element(By.XPATH, "//button[text()='Sign up']").click()
        time.sleep(5)

    def test_signup_alert(self, Browser):
        alert = Browser.switch_to.alert
        print(alert.text)
        alert.accept()
        time.sleep(5)

    def test_signup_close(self, Browser):
        # Browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/button[1]").click()
        Browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/button[1]").click()
        time.sleep(6)


