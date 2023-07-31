# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.wardrobe import Wardrobe  # noqa: E501
from openapi_server.test import BaseTestCase


class TestWardrobesController(BaseTestCase):
    """WardrobesController integration test stubs"""

    def test_wardrobes_get(self):
        """Test case for wardrobes_get

        Get all wardrobes
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/wardrobes',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_wardrobes_post(self):
        """Test case for wardrobes_post

        Add a new wardrobe
        """
        wardrobe = {"name":"name","location":"location","items":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/wardrobes',
            method='POST',
            headers=headers,
            data=json.dumps(wardrobe),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_wardrobes_wardrobe_id_delete(self):
        """Test case for wardrobes_wardrobe_id_delete

        Delete a wardrobe
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/wardrobes/{wardrobe_id}'.format(wardrobe_id='wardrobe_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_wardrobes_wardrobe_id_get(self):
        """Test case for wardrobes_wardrobe_id_get

        Get a wardrobe by ID
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/wardrobes/{wardrobe_id}'.format(wardrobe_id='wardrobe_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_wardrobes_wardrobe_id_put(self):
        """Test case for wardrobes_wardrobe_id_put

        Update a wardrobe
        """
        wardrobe = {"name":"name","location":"location","items":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/wardrobes/{wardrobe_id}'.format(wardrobe_id='wardrobe_id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(wardrobe),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
