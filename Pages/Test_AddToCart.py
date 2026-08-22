import time

from selenium.webdriver.common.by import By


class TestAddToCart:

    def test_AddTocart(self, Browser):
        Addtocartbtn = Browser.find_element(By.LINK_TEXT, "Add to cart")
        Addtocartbtn.click()
        time.sleep(6)

    def test_Dialogue(self, Browser):
        """Accept the 'product added' popup and hand its message back."""
        alert = Browser.switch_to.alert
        message = alert.text
        alert.accept()
        return message
