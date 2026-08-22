"""Assertion helpers for the demoblaze API.

demoblaze answers HTTP 200 to every request, successful or not.  A wrong
password, an unknown user and a malformed token all come back 200, so the
status code is only a transport-level signal -- the real outcome is in the
body, where failures appear as {"errorMessage": "..."}.

Every test goes through these two helpers so that quirk is handled in one
place instead of being repeated in a dozen files.
"""


def _assert_transport_ok(response):
    assert response.status_code == 200, (
        f"transport failure: {response.request.method} {response.request.url} "
        f"returned {response.status_code}"
    )


def assert_success(response):
    """Assert the call succeeded and return the parsed body.

    Returns None for endpoints that answer 200 with an empty body (/addtocart).
    """
    _assert_transport_ok(response)
    if not response.content:
        return None
    body = response.json()
    assert not (isinstance(body, dict) and "errorMessage" in body), (
        f"API returned an error: {body}"
    )
    return body


def assert_error(response, expected_message):
    """Assert the call failed with exactly `expected_message`."""
    _assert_transport_ok(response)
    body = response.json()
    assert isinstance(body, dict), f"expected an error object, got {body!r}"
    assert "errorMessage" in body, f"expected an errorMessage, got {body!r}"
    assert body["errorMessage"] == expected_message
