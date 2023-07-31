# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.wardrobe import Wardrobe  # noqa: F401


def test_wardrobes_get(client: TestClient):
    """Test case for wardrobes_get

    Get all wardrobes
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "GET",
        "/wardrobes",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_wardrobes_post(client: TestClient):
    """Test case for wardrobes_post

    Add a new wardrobe
    """
    wardrobe = {"name":"name","location":"location","items":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/wardrobes",
        headers=headers,
        json=wardrobe,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_wardrobes_wardrobe_id_delete(client: TestClient):
    """Test case for wardrobes_wardrobe_id_delete

    Delete a wardrobe
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/wardrobes/{wardrobeId}".format(wardrobeId='wardrobe_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_wardrobes_wardrobe_id_get(client: TestClient):
    """Test case for wardrobes_wardrobe_id_get

    Get a wardrobe by ID
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "GET",
        "/wardrobes/{wardrobeId}".format(wardrobeId='wardrobe_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_wardrobes_wardrobe_id_put(client: TestClient):
    """Test case for wardrobes_wardrobe_id_put

    Update a wardrobe
    """
    wardrobe = {"name":"name","location":"location","items":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/wardrobes/{wardrobeId}".format(wardrobeId='wardrobe_id_example'),
        headers=headers,
        json=wardrobe,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

