from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    samsung_product = (By.LINK_TEXT, "Samsung galaxy s6")
    add_to_cart_btn = (By.LINK_TEXT, "Add to cart")

    def select_product(self):

        product = self.wait.until(
            EC.element_to_be_clickable(self.samsung_product)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            product
        )

        self.driver.execute_script(
            "arguments[0].click();",
            product
        )

    def add_product_to_cart(self):

        add_btn = self.wait.until(
            EC.element_to_be_clickable(self.add_to_cart_btn)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            add_btn
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_btn
        )

        # Handle alert
        self.wait.until(EC.alert_is_present())

        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()