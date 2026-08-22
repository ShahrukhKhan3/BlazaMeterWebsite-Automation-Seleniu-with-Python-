"""Auth endpoints: /login and /signup.

/signup is covered by its duplicate-user case only. Registering a fresh user
would leave a permanent account on a shared public server -- demoblaze exposes
no way to delete one -- so the happy path is deliberately not tested here.
"""
import pytest

from API.asserts import assert_error, assert_success
from API.config import PASSWORD, USERNAME

pytestmark = pytest.mark.api

WRONG_PASSWORD = "Wrong password."
NO_SUCH_USER = "User does not exist."
DUPLICATE_USER = "This user already exist."


def test_login_returns_an_auth_token(client):
    body = assert_success(client.login(USERNAME, PASSWORD))
    assert body.startswith("Auth_token: "), f"unexpected login payload: {body!r}"
    assert body.split("Auth_token: ")[1], "token was empty"


@pytest.mark.parametrize("username, password, expected", [
    (USERNAME, "definitely-not-the-password", WRONG_PASSWORD),
    ("no_such_user_9931", PASSWORD, NO_SUCH_USER),
])
def test_login_rejects_bad_credentials(client, username, password, expected):
    assert_error(client.login(username, password), expected)


def test_signup_rejects_an_existing_user(client):
    assert_error(client.signup(USERNAME, PASSWORD), DUPLICATE_USER)
