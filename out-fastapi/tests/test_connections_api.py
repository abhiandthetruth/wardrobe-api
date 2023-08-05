# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.connections_add_post_request import ConnectionsAddPostRequest  # noqa: F401


def test_connections_add_post(client: TestClient):
    """Test case for connections_add_post

    Add a connection between users
    """
    connections_add_post_request = openapi_server.ConnectionsAddPostRequest()

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/connections/add",
        headers=headers,
        json=connections_add_post_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

