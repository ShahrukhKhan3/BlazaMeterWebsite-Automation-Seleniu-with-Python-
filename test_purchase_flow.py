
# 6️⃣ tests/test_purchase_flow.py
import time
from driver_setup import DriverSetup
from login_page import LoginPage
from product_page import ProductPage
from cart_page import CartPage
from order_page import OrderPage
# Driver setup

driver, wait = DriverSetup.get_driver()


# Page Objects

login = LoginPage(driver, wait)
product = ProductPage(driver, wait)
cart = CartPage(driver, wait)
order = OrderPage(driver, wait)


# Test Flow

# login.signup("Shahrukh", "12345")

login.login("Shahrukh", "12345")

product.select_product()

product.add_product_to_cart()

cart.open_cart()

cart.click_place_order()

order.fill_order_form(
    "Shahrukh",

    "4111111111111111"
)

order.purchase_product()

order.confirm_order()


# Close Browser

time.sleep(5)

print("Finished successfully")