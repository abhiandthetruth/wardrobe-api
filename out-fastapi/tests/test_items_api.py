# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.item import Item  # noqa: F401


def test_items_get(client: TestClient):
    """Test case for items_get

    Get all items
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "GET",
        "/items",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_items_item_id_delete(client: TestClient):
    """Test case for items_item_id_delete

    Delete an item
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/items/{item_id}".format(item_id='item_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_items_item_id_get(client: TestClient):
    """Test case for items_item_id_get

    Get an item by ID
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "GET",
        "/items/{item_id}".format(item_id='item_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_items_item_id_put(client: TestClient):
    """Test case for items_item_id_put

    Update an item
    """
    item = {"image":"image","size":"size","material":"material","name":"name","colors":["colors","colors"],"tags":["tags","tags"]}

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/items/{item_id}".format(item_id='item_id_example'),
        headers=headers,
        json=item,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_items_post(client: TestClient):
    """Test case for items_post

    Add a new item
    """
    item = {"image":"image","size":"size","material":"material","name":"name","colors":["colors","colors"],"tags":["tags","tags"]}

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/items",
        headers=headers,
        json=item,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

