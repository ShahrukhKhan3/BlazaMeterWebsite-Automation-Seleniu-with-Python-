"""Fixtures for the API suite.

Kept separate from the root conftest.py so the browser fixtures and the HTTP
fixtures never tangle.  Nothing here starts a browser.
"""
import uuid

import pytest

from API.client import DemoblazeClient
from API.config import PASSWORD, USERNAME


@pytest.fixture(scope="session")
def client():
    """One client, one requests.Session, reused for the whole run."""
    return DemoblazeClient()


@pytest.fixture(scope="session")
def token(client):
    """Log in once. demoblaze tokens are stable, so per-test logins buy nothing."""
    return client.token(USERNAME, PASSWORD)


@pytest.fixture
def cart_item(client, token):
    """Put one item in the cart and guarantee it is removed afterwards.

    demoblaze runs on a shared public server, so teardown matters: a yield
    fixture cleans up even when the test body fails.  The id is client-generated
    and unique per test, so concurrent items never delete each other.
    """
    item_id = f"pytest-{uuid.uuid4()}"
    client.add_to_cart(token, item_id, prod_id=1)
    yield item_id
    client.delete_item(token, item_id)   # /deleteitem, not /deletecart -- see README
