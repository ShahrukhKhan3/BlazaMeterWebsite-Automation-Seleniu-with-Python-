import time

from selenium.webdriver.common.by import By


class TestPurchase:
    def test_Purchase(self,Browser):
        purchase_btn = Browser.find_element(By.CSS_SELECTOR,"#orderModal > div > div > div.modal-footer > button.btn.btn-primary")
        purchase_btn.click()
        time.sleep(4)