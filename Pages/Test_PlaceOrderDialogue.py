from selenium.webdriver.common.by import By


class TestPlaceOrderDialogue:

    def test_PlaceOrderDialogueN(self, Browser):
        Browser.find_element(By.ID, "name").send_keys("shahrukh")

    def test_PlaceOrderDialogueC(self, Browser):
        Browser.find_element(By.ID, "card").send_keys("4111 1111 1111 1111")

    def get_entered_name(self, Browser):
        return Browser.find_element(By.ID, "name").get_attribute("value")

    def get_entered_card(self, Browser):
        return Browser.find_element(By.ID, "card").get_attribute("value")
