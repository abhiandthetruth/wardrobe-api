# coding: utf-8

import random
from fastapi.testclient import TestClient


from models.auth_login_post_request import AuthLoginPostRequest
from models.auth_register_post_request import AuthRegisterPostRequest  # noqa: F401


def test_register_and_then_login(client: TestClient):
    test_email_id = "emel@mail.com"
    test_name = "naem"
    test_password = "nkfklcnd"

    # Register
    register_user_post_request = AuthRegisterPostRequest(name=test_name, email_id=test_email_id, password=test_password).__dict__
    response = client.request(
        "POST",
        "/auth/register",
        json=register_user_post_request
    )
    assert response.status_code == 200

    # Login and verify
    auth_login_post_request = AuthLoginPostRequest(email_id=test_email_id, password=test_password).__dict__
    response = client.request(
        "POST",
        "auth/login",
        json=auth_login_post_request
    )

    assert response.status_code == 204
    assert response.headers.get("X-Auth-Token") != ""

