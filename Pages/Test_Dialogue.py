import time


class TestTDialogue:
    def test_Dialogue(self,Browser):
        time.sleep(6)
        alert = Browser.switch_to.alert
        print(alert.text)
        alert.accept()