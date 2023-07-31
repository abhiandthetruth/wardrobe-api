# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.connections_add_post_request import ConnectionsAddPostRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestConnectionsController(BaseTestCase):
    """ConnectionsController integration test stubs"""

    def test_connections_add_post(self):
        """Test case for connections_add_post

        Add a connection between users
        """
        connections_add_post_request = openapi_server.ConnectionsAddPostRequest()
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/connections/add',
            method='POST',
            headers=headers,
            data=json.dumps(connections_add_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
