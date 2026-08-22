import time

from selenium.webdriver.common.by import By


class TestCart:

    def test_Cart(self, Browser):
        Addtocartmenulink = Browser.find_element(By.ID, "cartur")
        Addtocartmenulink.click()
        time.sleep(5)

    def get_cart_titles(self, Browser):
        """Product names currently listed in the cart table."""
        rows = Browser.find_elements(By.CSS_SELECTOR, "#tbodyid tr td:nth-child(2)")
        return [row.text for row in rows]

    def get_cart_total(self, Browser):
        return int(Browser.find_element(By.ID, "totalp").text)
