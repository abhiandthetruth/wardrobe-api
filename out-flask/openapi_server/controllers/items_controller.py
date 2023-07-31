import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.item import Item  # noqa: E501
from openapi_server import util


def items_get():  # noqa: E501
    """Get all items

    Get a list of all wardrobe items. # noqa: E501


    :rtype: Union[List[Item], Tuple[List[Item], int], Tuple[List[Item], int, Dict[str, str]]
    """
    return 'do some magic!'


def items_item_id_delete(item_id):  # noqa: E501
    """Delete an item

    Delete a wardrobe item. # noqa: E501

    :param item_id: 
    :type item_id: str
    :type item_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def items_item_id_get(item_id):  # noqa: E501
    """Get an item by ID

    Get a specific wardrobe item by its ID. # noqa: E501

    :param item_id: 
    :type item_id: str
    :type item_id: str

    :rtype: Union[Item, Tuple[Item, int], Tuple[Item, int, Dict[str, str]]
    """
    return 'do some magic!'


def items_item_id_put(item_id, item):  # noqa: E501
    """Update an item

    Update an existing wardrobe item. # noqa: E501

    :param item_id: 
    :type item_id: str
    :type item_id: str
    :param item: 
    :type item: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        item = Item.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def items_post(item):  # noqa: E501
    """Add a new item

    Create a new wardrobe item. # noqa: E501

    :param item: 
    :type item: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        item = Item.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
