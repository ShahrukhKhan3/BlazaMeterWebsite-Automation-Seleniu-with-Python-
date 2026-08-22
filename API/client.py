"""Service object for the demoblaze REST API.

The API layer's equivalent of the page objects in Pages/: tests describe what
they want, this class knows how demoblaze wants to be asked.  Three of its
quirks are handled here and nowhere else:

  * passwords travel base64-encoded, so "12345" goes out as "MTIzNDU="
  * a successful /login answers with the bare string "Auth_token: <token>"
  * the token is sent in the request *body* as "cookie", not as a header
"""
import base64

import requests

from API.asserts import assert_success
from API.config import BASE_URL


class DemoblazeClient:

    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def _post(self, path, payload):
        return self.session.post(f"{self.base_url}/{path}", json=payload)

    @staticmethod
    def _encode(password):
        return base64.b64encode(password.encode()).decode()

    # ------------------------------------------------------------------ catalogue

    def entries(self):
        return self.session.get(f"{self.base_url}/entries")

    def by_category(self, category):
        return self._post("bycat", {"cat": category})

    def view(self, product_id):
        return self._post("view", {"id": str(product_id)})

    # ----------------------------------------------------------------------- auth

    def login(self, username, password):
        return self._post("login", {"username": username,
                                    "password": self._encode(password)})

    def signup(self, username, password):
        return self._post("signup", {"username": username,
                                     "password": self._encode(password)})

    def token(self, username, password):
        """Log in and return just the token string."""
        body = assert_success(self.login(username, password))
        assert isinstance(body, str) and body.startswith("Auth_token: "), (
            f"unexpected login payload: {body!r}"
        )
        return body.split("Auth_token: ")[1]

    # ----------------------------------------------------------------------- cart

    def add_to_cart(self, token, item_id, prod_id):
        return self._post("addtocart", {"id": item_id, "cookie": token,
                                        "prod_id": prod_id, "flag": True})

    def view_cart(self, token):
        return self._post("viewcart", {"cookie": token, "flag": True})

    def cart_item_ids(self, token):
        """The ids currently in `token`'s cart."""
        body = assert_success(self.view_cart(token))
        return [item["id"] for item in body["Items"]]

    def delete_cart(self, token, item_id):
        """Broken upstream -- reports success and deletes nothing. Use delete_item."""
        return self._post("deletecart", {"cookie": token, "id": item_id, "flag": True})

    def delete_item(self, token, item_id):
        return self._post("deleteitem", {"cookie": token, "id": item_id, "flag": True})
