"""Catalogue endpoints: /entries, /bycat, /view."""
import pytest

from API.asserts import assert_success

pytestmark = pytest.mark.api

PRODUCT_FIELDS = {"id", "cat", "title", "price", "img", "desc"}


def test_entries_returns_the_catalogue(client):
    body = assert_success(client.entries())
    assert body["Items"], "catalogue came back empty"
    for item in body["Items"]:
        missing = PRODUCT_FIELDS - set(item)
        assert not missing, f"product {item.get('id')} is missing {missing}"
        assert isinstance(item["price"], (int, float)), \
            f"product {item['id']} has a non-numeric price: {item['price']!r}"
        assert item["title"], f"product {item['id']} has an empty title"


@pytest.mark.parametrize("category", ["phone", "notebook", "monitor"])
def test_bycat_returns_only_that_category(client, category):
    body = assert_success(client.by_category(category))
    assert body["Items"], f"no products came back for category {category!r}"
    assert {item["cat"] for item in body["Items"]} == {category}


def test_bycat_unknown_category_returns_an_empty_list(client):
    body = assert_success(client.by_category("no_such_category"))
    assert body["Items"] == []


def test_view_returns_a_single_product(client):
    body = assert_success(client.view(1))
    assert body["id"] == 1
    assert body["title"] == "Samsung galaxy s6"
    assert body["price"] == 360.0
