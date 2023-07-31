# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.auth_login_post_request import AuthLoginPostRequest  # noqa: F401


def test_auth_login_post(client: TestClient):
    """Test case for auth_login_post

    Authenticate user
    """
    auth_login_post_request = openapi_server.AuthLoginPostRequest()

    headers = {
    }
    response = client.request(
        "POST",
        "/auth/login",
        headers=headers,
        json=auth_login_post_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

