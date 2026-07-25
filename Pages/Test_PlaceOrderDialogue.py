from selenium.webdriver.common.by import By


class TestPlaceOrderDialogue:
    def test_PlaceOrderDialogueN(self, Browser):
        Orderplacebtn = Browser.find_element(By.ID, "name").send_keys("shahrukh")

    def test_PlaceOrderDialogueC(self, Browser):
        Orderplacebtn1 = Browser.find_element(By.ID, "card").send_keys("4111 1111 1111 1111")