import time

from selenium.webdriver.common.by import By


class TestOK:

    def test_OK(self, Browser):
        ok_btn = Browser.find_element(By.XPATH, "//button[text()='OK']")
        time.sleep(1)
        ok_btn.click()
        time.sleep(3)

    def get_current_url(self, Browser):
        return Browser.current_url

    def get_cart_titles(self, Browser):
        """Reopen the cart and list what is left in it."""
        Browser.find_element(By.ID, "cartur").click()
        time.sleep(5)
        rows = Browser.find_elements(By.CSS_SELECTOR, "#tbodyid tr td:nth-child(2)")
        return [row.text for row in rows]
