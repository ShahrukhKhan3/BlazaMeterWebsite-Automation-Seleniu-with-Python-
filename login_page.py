from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    signup_link = (By.ID, "signin2")
    signup_username = (By.ID, "sign-username")
    signup_password = (By.ID, "sign-password")
    signup_button = (By.XPATH, "//button[text()='Sign up']")

    login_link = (By.ID, "login2")
    login_username = (By.ID, "loginusername")
    login_password = (By.ID, "loginpassword")
    login_button = (By.XPATH, "//button[text()='Log in']")

    def signup(self, username, password):
        print(username)

        self.driver.find_element(*self.signup_link).click()

        self.wait.until(
            EC.visibility_of_element_located(self.signup_username)
        ).send_keys(username)

        self.driver.find_element(*self.signup_password).send_keys(password)

        self.driver.find_element(*self.signup_button).click()

        # Handle alert
        self.wait.until(EC.alert_is_present())

        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()

        # Close modal
        close_btn = self.driver.find_element(
            By.XPATH,
            "//div[@id='signInModal']//button[text()='Close']"
        )
        close_btn.click()

        self.wait.until(
            EC.invisibility_of_element_located((By.ID, "signInModal"))
        )

    def login(self, username, password):

        self.driver.find_element(*self.login_link).click()

        self.wait.until(
            EC.visibility_of_element_located(self.login_username)
        ).send_keys(username)

        self.driver.find_element(*self.login_password).send_keys(password)

        self.driver.find_element(*self.login_button).click()