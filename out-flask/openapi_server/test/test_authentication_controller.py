# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.auth_login_post_request import AuthLoginPostRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestAuthenticationController(BaseTestCase):
    """AuthenticationController integration test stubs"""

    def test_auth_login_post(self):
        """Test case for auth_login_post

        Authenticate user
        """
        auth_login_post_request = openapi_server.AuthLoginPostRequest()
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v1/auth/login',
            method='POST',
            headers=headers,
            data=json.dumps(auth_login_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
