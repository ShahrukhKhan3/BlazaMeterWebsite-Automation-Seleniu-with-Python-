from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

wait = WebDriverWait(driver, 10)


def open_website():
    driver.get("https://demoblaze.com/")


def click_signup():
    driver.find_element(By.ID, "signin2").click()


def sign_username():
    wait.until(
        EC.visibility_of_element_located((By.ID, "sign-username"))
    ).send_keys("Shahrukh")


def sign_password():
    driver.find_element(By.ID, "sign-password").send_keys("12345")


def click_signup_button():
    driver.find_element(
        By.XPATH,
        "//button[text()='Sign up']"
    ).click()
def signup_alert():
    wait.until(EC.alert_is_present())

    alert = driver.switch_to.alert

    print(alert.text)

    alert.accept()
def signup_close():
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/button[1]").click()

def click_login():
    driver.find_element(By.ID, "login2").click()


def enter_username():
    time.sleep(2)
    driver.find_element(By.ID, "loginusername").send_keys("Shahrukh")


def enter_password():
    driver.find_element(By.ID, "loginpassword").send_keys("12345")


def click_login_button():
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()
    time.sleep(5)
def Click_Product():
    product = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6"))

    )
    product.click()
    time.sleep(5)
def AddTocart():

    Addtocartbtn = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart"))
    )

    Addtocartbtn.click()
def Dialogue():

    wait.until(EC.alert_is_present())

    alert = driver.switch_to.alert

    print(alert.text)

    alert.accept()   # ✅ THIS IS MISSING IN YOUR CODE
def Cart():
    Addtocartmenulink = wait.until(
        EC.element_to_be_clickable((By.ID, "cartur"))
    )
    Addtocartmenulink.click()
    time.sleep(5)
def PlaceOrder():

    Orderplacebtn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[6]/div/div[2]/button")
        )
    )

    Orderplacebtn.click()
def PlaceOrderDialogueN():

    PODialogue = wait.until(
        EC.element_to_be_clickable((By.ID, "name")))
    PODialogue.send_keys("Shahrukh")
    time.sleep(5)
# Calling Functions
def PlaceOrderDialogueC():

    PODialogue = wait.until(
        EC.element_to_be_clickable((By.ID, "card")))

    PODialogue.send_keys("4111 1111 1111 1111")


def Purchase():
    purchase_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,"#orderModal > div > div > div.modal-footer > button.btn.btn-primary")))
    purchase_btn.click()


def Purchase():

    purchase_btn = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Purchase']"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", purchase_btn)
    time.sleep(1)

    driver.execute_script("arguments[0].click();", purchase_btn)
def OK():

    ok_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", ok_btn)
    time.sleep(1)

    driver.execute_script("arguments[0].click();", ok_btn)



open_website()

time.sleep(2)

click_signup()

sign_username()

sign_password()

click_signup_button()
signup_alert()
time.sleep(5)
signup_close()
time.sleep(5)
click_login()
enter_username()
enter_password()
click_login_button()
Click_Product()
AddTocart()
Dialogue()
time.sleep(5)
Cart()
PlaceOrder()
PlaceOrderDialogueN()
PlaceOrderDialogueC()
Purchase()
OK()