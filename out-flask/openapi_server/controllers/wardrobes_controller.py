import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.wardrobe import Wardrobe  # noqa: E501
from openapi_server import util


def wardrobes_get():  # noqa: E501
    """Get all wardrobes

    Get a list of all user&#39;s wardrobes. # noqa: E501


    :rtype: Union[List[Wardrobe], Tuple[List[Wardrobe], int], Tuple[List[Wardrobe], int, Dict[str, str]]
    """
    return 'do some magic!'


def wardrobes_post(wardrobe):  # noqa: E501
    """Add a new wardrobe

    Create a new wardrobe for the user. # noqa: E501

    :param wardrobe: 
    :type wardrobe: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        wardrobe = Wardrobe.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def wardrobes_wardrobe_id_delete(wardrobe_id):  # noqa: E501
    """Delete a wardrobe

    Delete an existing wardrobe. # noqa: E501

    :param wardrobe_id: 
    :type wardrobe_id: str
    :type wardrobe_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def wardrobes_wardrobe_id_get(wardrobe_id):  # noqa: E501
    """Get a wardrobe by ID

    Get a specific wardrobe by its ID. # noqa: E501

    :param wardrobe_id: 
    :type wardrobe_id: str
    :type wardrobe_id: str

    :rtype: Union[Wardrobe, Tuple[Wardrobe, int], Tuple[Wardrobe, int, Dict[str, str]]
    """
    return 'do some magic!'


def wardrobes_wardrobe_id_put(wardrobe_id, wardrobe):  # noqa: E501
    """Update a wardrobe

    Update an existing wardrobe. # noqa: E501

    :param wardrobe_id: 
    :type wardrobe_id: str
    :type wardrobe_id: str
    :param wardrobe: 
    :type wardrobe: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        wardrobe = Wardrobe.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
