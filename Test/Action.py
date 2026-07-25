import time

import pytest
from selenium.webdriver.common.by import By

from Pages.Test_click_signup import TestSignup
from Pages.Test_Login import TestLogin
from Pages.Test_ClickProduct import TestClickProduct
from Pages.Test_AddToCart import TestAddToCart
from Pages.Test_Cart import TestCart
from Pages.Test_PlaceOrder import TestPlaceOrder
from Pages.Test_PlaceOrderDialogue import TestPlaceOrderDialogue
from Pages.Test_Purchase import TestPurchase
# from Pages.Test_Dialogue import TestTDialogue
from Pages.Test_OK import TestOK



class Action:

    def Action(self,Browser):
        Signup= TestSignup()
        Signup.test_click_signup(Browser)
        Signup.test_signup_alert(Browser)
        Signup.test_signup_close(Browser)
        Login=TestLogin()
        Login.test_click_login(Browser)
        Login.test_enter_username(Browser)
        Login.test_enter_password(Browser)
        Login.test_click_login_button(Browser)
        Clickp=TestClickProduct()
        Clickp.test_Click_Product(Browser)
        AddToCart=TestAddToCart()
        AddToCart.test_AddTocart(Browser)
        AddToCart.test_Dialogue(Browser)
        time.sleep(5)
        # TestTDialogues=TestTDialogue(Browser)
        # TestTDialogues.test_Dialogue()
        TestsCart= TestCart()
        TestsCart.test_Cart(Browser)
        PlaceOrder = TestPlaceOrder()
        PlaceOrder.test_PlaceOrder(Browser)
        PlaceOrderD=TestPlaceOrderDialogue()
        PlaceOrderD.test_PlaceOrderDialogueN(Browser)
        PlaceOrderD.test_PlaceOrderDialogueC(Browser)
        TTestPurchase=TestPurchase()
        TTestPurchase.test_Purchase(Browser)
        Okk=TestOK()
        Okk.test_OK(Browser)




