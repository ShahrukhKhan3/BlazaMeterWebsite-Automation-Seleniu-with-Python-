import time

from _pytest import unittest
from selenium.webdriver.common.bidi.browser import Browser
from selenium.webdriver.common.by import By
from self import self


class TestLogin:

    def test_click_login(self,Browser):
         Browser.find_element(By.ID, "login2").click()
    def test_enter_username(self,Browser):
         time.sleep(2)
         Browser.find_element(By.ID, "loginusername").send_keys("Shahrukh")
    def test_enter_password(self,Browser):
         Browser.find_element(By.ID, "loginpassword").send_keys("12345")
    def test_click_login_button(self,Browser):
         Browser.find_element(By.XPATH, "//button[text()='Log in']").click()
         time.sleep(7)              