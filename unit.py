import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestGoogle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_open_google(self):
        self.driver.get("https://www.google.com")

        title = self.driver.title

        self.assertIn("Google", title)

    def tearDown(self):
        print("Close Website")
if __name__ == "__main__":
    unittest.main()