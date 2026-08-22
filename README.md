# demoblaze automation — UI (Selenium) + API (requests)

Two test suites over [demoblaze.com](https://demoblaze.com), sharing one pytest
runner, one report format and one repo.

| Layer | Location | Driver | Marker |
|---|---|---|---|
| UI  | `Pages/`, `Test/`, `test_purchase_flow.py` | Selenium + Firefox | `ui`  |
| API | `API/`                                    | `requests`         | `api` |

Selenium plays no part in the API suite. Selenium speaks WebDriver to a browser;
it cannot make HTTP assertions. The API tests talk straight to
`https://api.demoblaze.com` with `requests` and never open a browser.

## Running

```bash
pip install -r requirements.txt

pytest -m api      # API suite, no browser
pytest -m ui       # Selenium purchase flow
pytest             # both

pytest -m api --html=reports/api_report.html --self-contained-html
```

`--html` is deliberately not in `addopts`: a baked-in path would make an API run
overwrite the UI report and lose its failure screenshots.

## Configuration

`API/config.py` reads the environment, defaulting to a public demo account:

| Variable | Default |
|---|---|
| `DEMOBLAZE_URL`  | `https://api.demoblaze.com` |
| `DEMOBLAZE_USER` | `Shahrukh` |
| `DEMOBLAZE_PASS` | `12345` |

## What we learned about this API

Four things established by probing the live service. None are recoverable from
reading the test code, and the first two change how the tests must be written.

**1. Every response is HTTP 200.** Wrong password, unknown user, duplicate
signup, malformed token, garbage input — all 200. `assert r.status_code == 200`
therefore passes on failures and is not a functional assertion. Errors are
identified by an `errorMessage` key in the body. `API/asserts.py` holds this in
one place; the status check survives there only as a transport-level guard
against DNS failures and 5xx.

**2. `/deletecart` is broken.** It answers `"Item deleted."` and the item stays
in the cart — confirmed across repeated calls, so it is not a timing effect.
`/deleteitem` is the endpoint that actually deletes.

```
POST /deletecart -> "Item deleted."   then  /viewcart -> item still present
POST /deleteitem -> "Item deleted."   then  /viewcart -> {"Items":[]}
```

`test_deletecart_removes_the_item` asserts the *correct* behaviour under
`@pytest.mark.xfail(strict=True)`. It reports as `xfailed` today; if demoblaze
ever fixes the endpoint the test XPASSes and fails the run, prompting removal of
the marker. Cleanup everywhere else uses `/deleteitem`.

**3. Passwords are base64 in the API.** The browser encodes before sending, so
the API expects `MTIzNDU=`, not `12345`. `DemoblazeClient` encodes on the way out.

**4. The auth token is not a header.** A successful `/login` answers with the
bare JSON *string* `"Auth_token: <token>"` — not an object, so `r.json()["..."]`
raises `TypeError` on success. The token is then passed back in the request
**body** as `cookie`.

Two smaller notes: `/addtocart` answers 200 with an empty body, so `.json()`
raises `JSONDecodeError` — `assert_success` returns `None` for empty responses.
And cart item ids are **client-generated**: you invent the id and send it, which
is how teardown knows what to remove.

## Test data policy

demoblaze is a shared public server and exposes no way to delete a user, so any
account a test creates is permanent. The suite therefore:

* reuses the existing `Shahrukh` account rather than generating users;
* covers `/signup` through its duplicate-user case only — real coverage, zero
  new data, at the cost of the happy path;
* adds cart items with a `uuid4` id and removes them in fixture teardown, which
  runs even when the test body fails.

## Known rough edge

`Pages/*.py` are page objects named `Test_Login.py` / `class TestLogin` /
`def test_click_login`. They match pytest's collection patterns, so pytest used
to collect all 17 methods as standalone tests and fire them out of order
alongside the real flow. `norecursedirs = Pages Test` in `pytest.ini` stops the
collection; renaming them to `login_page.py` / `class LoginPage` / `def click_login`
is the real fix and is still outstanding.
