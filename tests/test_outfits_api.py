# coding: utf-8

from fastapi.testclient import TestClient


from models.outfit import Outfit  # noqa: F401


def test_outfits_get(client: TestClient):
    """Test case for outfits_get

    Get all outfits
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "GET",
        "/outfits",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_outfits_outfit_id_delete(client: TestClient):
    """Test case for outfits_outfit_id_delete

    Delete an outfit
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/outfits/{outfitId}".format(outfitId='outfit_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_outfits_outfit_id_get(client: TestClient):
    """Test case for outfits_outfit_id_get

    Get an outfit by ID
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "GET",
        "/outfits/{outfitId}".format(outfitId='outfit_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_outfits_outfit_id_put(client: TestClient):
    """Test case for outfits_outfit_id_put

    Update an outfit
    """
    outfit = {"bottomwears":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"accessories":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","topwears":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"footwears":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/outfits/{outfitId}".format(outfitId='outfit_id_example'),
        headers=headers,
        json=outfit,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_outfits_post(client: TestClient):
    """Test case for outfits_post

    Add a new outfit
    """
    outfit = {"bottomwears":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"accessories":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","topwears":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"footwears":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/outfits",
        headers=headers,
        json=outfit,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

