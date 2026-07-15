import pytest
from selenium import webdriver
from selenium.webdriver.common.bidi.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestMyPytest():

    def test_open_website(self,Browser):
        assert "STORE" in Browser.title
    def test_click_signup(self,Browser):
        Browser.find_element(By.ID, "signin2").click()
        time.sleep(3)
        Browser.find_element(By.ID, "sign-usernames").send_keys("Shahrukh")
        Browser.find_element(By.ID, "sign-password").send_keys("12345")
        Browser.find_element(By.XPATH, "//button[text()='Sign up']").click()
        time.sleep(5)
    def test_signup_alert(self,Browser):
         alert = Browser.switch_to.alert
         print(alert.text)
         alert.accept()
         time.sleep(5)

    def test_signup_close(self,Browser):
         # Browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/button[1]").click()
        Browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/button[1]").click()
        time.sleep(6)
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
    def test_Click_Product(self,Browser):
        product = Browser.find_element(By.LINK_TEXT, "Samsung galaxy s6")
        product.click()
        time.sleep(5)
    def test_AddTocart(self,Browser):
        Addtocartbtn = Browser.find_element(By.LINK_TEXT, "Add to cart")
        Addtocartbtn.click()
        time.sleep(6)
    def test_Dialogue(self,Browser):
        alert = Browser.switch_to.alert
        print(alert.text)
        alert.accept()   # ✅ THIS IS MISSING IN YOUR CODE
    def test_Cart(self,Browser):
        Addtocartmenulink = Browser.find_element(By.ID, "cartur")
        Addtocartmenulink.click()
        time.sleep(5)
    def test_PlaceOrder(self,Browser):
        Orderplacebtn = Browser.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/button")
        Orderplacebtn.click()
        time.sleep(6)
    def test_PlaceOrderDialogueN(self,Browser):
        Orderplacebtn = Browser.find_element(By.ID, "name").send_keys("shahrukh")
    def test_PlaceOrderDialogueC(self,Browser):
        Orderplacebtn1 = Browser.find_element(By.ID, "card").send_keys("4111 1111 1111 1111")
    # def test_PlaceOrderDialogueN(self,Browser):
    #     Browser.find_element(By.ID, "name").send_keys("shahrukh")
    #  def test_PlaceOrderDialogueC(self,Browser):
    #     Browser.find_element(By.ID, "card").send_keys("4111 1111 1111 1111")
    def test_Purchase(self,Browser):
        purchase_btn = Browser.find_element(By.CSS_SELECTOR,"#orderModal > div > div > div.modal-footer > button.btn.btn-primary")
        purchase_btn.click()
        time.sleep(4)

    # def test_Purchase(self,Browser):
    #  purchase_btn = Browser.find_element(By.XPATH, "//button[text()='Purchase']")
    #  time.sleep(1)
    #  purchase_btn.click()
    def test_OK(self,Browser):
     ok_btn = Browser.find_element(By.XPATH, "//button[text()='OKK']")
     time.sleep(1)
     ok_btn.click()


#
#
#
#
# time.sleep(2)
#
# click_signup()
#
# sign_username()
#
# sign_password()
#
# click_signup_button()
# signup_alert()
# time.sleep(5)
# signup_close()
# time.sleep(5)
# click_login()
# enter_username()
# enter_password()
# click_login_button()
# Click_Product()
# AddTocart()
# Dialogue()
# time.sleep(5)
# Cart()
# PlaceOrder()
# PlaceOrderDialogueN()
# PlaceOrderDialogueC()
# Purchase()
# OK()