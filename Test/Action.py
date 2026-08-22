"""The purchase journey, step by step, with a check after every step.

Each page object knows how to *do* something and how to *read* the page back.
This file is where the reading turns into a pass or a fail: every click is
followed by an assertion that says what the site was supposed to do.
"""
import time

from Pages.Test_AddToCart import TestAddToCart
from Pages.Test_Cart import TestCart
from Pages.Test_ClickProduct import TestClickProduct
from Pages.Test_Login import TestLogin
from Pages.Test_OK import TestOK
from Pages.Test_PlaceOrder import TestPlaceOrder
from Pages.Test_PlaceOrderDialogue import TestPlaceOrderDialogue
from Pages.Test_Purchase import TestPurchase
from Pages.Test_click_signup import TestSignup

USERNAME = "Shahrukh"
PRODUCT = "Samsung galaxy s6"
PRICE = 360
BUYER_NAME = "shahrukh"
CARD = "4111 1111 1111 1111"


class Action:

    def Action(self, Browser):

        # --- sign up -------------------------------------------------------
        # Shahrukh was registered long ago, so demoblaze must reject the repeat
        # attempt. A "Sign up successful." here would mean the account vanished.
        Signup = TestSignup()
        Signup.test_click_signup(Browser)
        message = Signup.test_signup_alert(Browser)
        assert message == "This user already exist.",             f"unexpected sign-up message: {message!r}"
        Signup.test_signup_close(Browser)

        # --- log in --------------------------------------------------------
        Login = TestLogin()
        Login.test_click_login(Browser)
        Login.test_enter_username(Browser)
        Login.test_enter_password(Browser)
        Login.test_click_login_button(Browser)
        welcome = Login.get_welcome_text(Browser)
        assert welcome == f"Welcome {USERNAME}",             f"login did not complete, navbar says {welcome!r}"
        assert Login.is_logout_visible(Browser), "Log out link is not showing"

        # --- open the product ----------------------------------------------
        Clickp = TestClickProduct()
        Clickp.test_Click_Product(Browser)
        title = Clickp.get_product_title(Browser)
        price = Clickp.get_product_price(Browser)
        assert title == PRODUCT, f"opened the wrong product: {title!r}"
        assert price == PRICE, f"expected ${PRICE}, the page says ${price}"

        # --- add it to the cart ---------------------------------------------
        AddToCart = TestAddToCart()
        AddToCart.test_AddTocart(Browser)
        added = AddToCart.test_Dialogue(Browser)
        assert added == "Product added.", f"unexpected add-to-cart message: {added!r}"
        time.sleep(5)

        # --- check the cart --------------------------------------------------
        TestsCart = TestCart()
        TestsCart.test_Cart(Browser)
        titles = TestsCart.get_cart_titles(Browser)
        total = TestsCart.get_cart_total(Browser)
        assert titles == [PRODUCT], f"cart holds {titles} instead of one {PRODUCT}"
        assert total == PRICE, f"cart total is {total}, expected {PRICE}"

        # --- open the order form ---------------------------------------------
        PlaceOrder = TestPlaceOrder()
        PlaceOrder.test_PlaceOrder(Browser)
        assert PlaceOrder.is_order_form_open(Browser), "the order form did not open"
        assert PlaceOrder.get_order_total(Browser) == PRICE,             "the order form total does not match the cart"

        # --- fill the order form ----------------------------------------------
        PlaceOrderD = TestPlaceOrderDialogue()
        PlaceOrderD.test_PlaceOrderDialogueN(Browser)
        PlaceOrderD.test_PlaceOrderDialogueC(Browser)
        assert PlaceOrderD.get_entered_name(Browser) == BUYER_NAME, "the name did not type in"
        assert PlaceOrderD.get_entered_card(Browser) == CARD, "the card number did not type in"

        # --- buy ----------------------------------------------------------------
        TTestPurchase = TestPurchase()
        TTestPurchase.test_Purchase(Browser)
        confirmation = TTestPurchase.get_confirmation_text(Browser)
        assert "Thank you for your purchase!" in confirmation,             f"no confirmation, the panel says {confirmation!r}"
        assert f"Amount: {PRICE} USD" in confirmation,             f"confirmation shows the wrong amount: {confirmation!r}"
        assert CARD in confirmation, "confirmation shows the wrong card number"

        # --- dismiss, and confirm the cart was emptied ----------------------------
        Okk = TestOK()
        Okk.test_OK(Browser)
        assert "index.html" in Okk.get_current_url(Browser),             "did not return to the home page after the purchase"
        assert Okk.get_cart_titles(Browser) == [],             "the cart still has items in it after a completed purchase"
