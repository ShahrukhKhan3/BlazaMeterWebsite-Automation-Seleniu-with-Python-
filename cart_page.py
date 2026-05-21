
# 4️⃣ pages/cart_page.py


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    cart_link = (By.ID, "cartur")
    place_order_btn = (By.XPATH, "//button[text()='Place Order']")

    def open_cart(self):

        cart = self.wait.until(
            EC.element_to_be_clickable(self.cart_link)
        )

        cart.click()

    def click_place_order(self):

        place_order = self.wait.until(
            EC.element_to_be_clickable(self.place_order_btn)
        )

        place_order.click()
