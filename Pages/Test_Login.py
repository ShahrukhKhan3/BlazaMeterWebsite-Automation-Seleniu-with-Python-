import time

from selenium.webdriver.common.by import By


class TestLogin:

    def test_click_login(self, Browser):
        Browser.find_element(By.ID, "login2").click()

    def test_enter_username(self, Browser):
        time.sleep(2)
        Browser.find_element(By.ID, "loginusername").send_keys("Shahrukh")

    def test_enter_password(self, Browser):
        Browser.find_element(By.ID, "loginpassword").send_keys("12345")

    def test_click_login_button(self, Browser):
        Browser.find_element(By.XPATH, "//button[text()='Log in']").click()
        time.sleep(7)

    def get_welcome_text(self, Browser):
        """The 'Welcome <user>' label the navbar shows once logged in."""
        return Browser.find_element(By.ID, "nameofuser").text

    def is_logout_visible(self, Browser):
        """Log out only appears for a logged-in user."""
        return Browser.find_element(By.ID, "logout2").is_displayed()
