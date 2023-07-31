# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.item import Item  # noqa: E501
from openapi_server.test import BaseTestCase


class TestItemsController(BaseTestCase):
    """ItemsController integration test stubs"""

    def test_items_get(self):
        """Test case for items_get

        Get all items
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/items',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_item_id_delete(self):
        """Test case for items_item_id_delete

        Delete an item
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/items/{item_id}'.format(item_id='item_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_item_id_get(self):
        """Test case for items_item_id_get

        Get an item by ID
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/items/{item_id}'.format(item_id='item_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_item_id_put(self):
        """Test case for items_item_id_put

        Update an item
        """
        item = {"image":"image","size":"size","material":"material","name":"name","colors":["colors","colors"],"tags":["tags","tags"]}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/items/{item_id}'.format(item_id='item_id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(item),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_post(self):
        """Test case for items_post

        Add a new item
        """
        item = {"image":"image","size":"size","material":"material","name":"name","colors":["colors","colors"],"tags":["tags","tags"]}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/items',
            method='POST',
            headers=headers,
            data=json.dumps(item),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
