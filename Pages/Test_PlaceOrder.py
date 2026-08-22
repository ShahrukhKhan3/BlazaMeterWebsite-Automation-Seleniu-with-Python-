import time

from selenium.webdriver.common.by import By


class TestPlaceOrder:

    def test_PlaceOrder(self, Browser):
        Orderplacebtn = Browser.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/button")
        Orderplacebtn.click()
        time.sleep(6)

    def is_order_form_open(self, Browser):
        return Browser.find_element(By.ID, "orderModal").is_displayed()

    def get_order_total(self, Browser):
        """Reads 'Total: 360' from the order form and returns 360."""
        raw = Browser.find_element(By.ID, "totalm").text
        return int(raw.split(":")[1].strip())
