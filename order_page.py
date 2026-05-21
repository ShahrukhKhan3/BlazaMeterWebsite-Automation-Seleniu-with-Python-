from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class OrderPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # ✅ ONLY REQUIRED FIELDS
    name_field = (By.ID, "name")
    card_field = (By.ID, "card")

    purchase_btn = (By.XPATH, "//button[text()='Purchase']")
    ok_btn = (By.XPATH, "//button[text()='OK']")

    # ✅ FILL ONLY NAME + CARD
    def fill_order_form(self, name, card):

        self.wait.until(
            EC.visibility_of_element_located(self.name_field)
        ).send_keys(name)

        self.driver.find_element(*self.card_field).send_keys(card)

    # ✅ PURCHASE BUTTON
    def purchase_product(self):

        purchase = self.wait.until(
            EC.element_to_be_clickable(self.purchase_btn)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            purchase
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            purchase
        )

    # ✅ OK BUTTON
    def confirm_order(self):

        ok = self.wait.until(
            EC.element_to_be_clickable(self.ok_btn)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            ok
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            ok
        )