import time

from selenium.webdriver.common.by import By


class TestClickProduct:

    def test_Click_Product(self, Browser):
        time.sleep(7)
        Prod = Browser.find_element(By.LINK_TEXT, "Samsung galaxy s6")
        Prod.click()
        time.sleep(5)

    def get_product_title(self, Browser):
        return Browser.find_element(By.CSS_SELECTOR, "h2.name").text

    def get_product_price(self, Browser):
        """Reads '$360 *includes tax' and returns just the number, 360."""
        raw = Browser.find_element(By.CSS_SELECTOR, "h3.price-container").text
        return int(raw.split("$")[1].split("*")[0].strip())
