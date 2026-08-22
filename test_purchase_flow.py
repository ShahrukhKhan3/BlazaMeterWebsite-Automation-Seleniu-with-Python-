import pytest
from Test.Action import Action


@pytest.mark.ui
class TestPurchaseFlow:

    def test_purchase_flow(self, Browser):
        flow = Action()
        flow.Action(Browser)    # or flow.Action(Browser) if you haven't renamed it