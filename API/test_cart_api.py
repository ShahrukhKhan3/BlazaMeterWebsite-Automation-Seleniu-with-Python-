"""Cart endpoints: /addtocart, /viewcart, /deletecart, /deleteitem.

The cart_item fixture adds an item and removes it in teardown, so these tests
leave nothing behind on the shared server even when they fail.
"""
import pytest

from API.asserts import assert_error, assert_success

pytestmark = pytest.mark.api

MALFORMED_TOKEN = "Bad parameter, token malformed."


def test_addtocart_puts_the_item_in_the_cart(client, token, cart_item):
    assert cart_item in client.cart_item_ids(token)


def test_viewcart_rejects_a_malformed_token(client):
    assert_error(client.view_cart("totally-invalid-token"), MALFORMED_TOKEN)


@pytest.mark.xfail(
    strict=True,
    reason="demoblaze bug: /deletecart answers 'Item deleted.' but the item stays "
           "in the cart. If this XPASSes, the bug is fixed -- drop the marker.",
)
def test_deletecart_removes_the_item(client, token, cart_item):
    assert_success(client.delete_cart(token, cart_item))
    assert cart_item not in client.cart_item_ids(token)


def test_deleteitem_removes_the_item(client, token, cart_item):
    assert_success(client.delete_item(token, cart_item))
    assert cart_item not in client.cart_item_ids(token)
