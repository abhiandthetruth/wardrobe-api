import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.outfit import Outfit  # noqa: E501
from openapi_server import util


def outfits_get():  # noqa: E501
    """Get all outfits

    Get a list of all created outfits. # noqa: E501


    :rtype: Union[List[Outfit], Tuple[List[Outfit], int], Tuple[List[Outfit], int, Dict[str, str]]
    """
    return 'do some magic!'


def outfits_outfit_id_delete(outfit_id):  # noqa: E501
    """Delete an outfit

    Delete an existing outfit. # noqa: E501

    :param outfit_id: 
    :type outfit_id: str
    :type outfit_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def outfits_outfit_id_get(outfit_id):  # noqa: E501
    """Get an outfit by ID

    Get a specific outfit by its ID. # noqa: E501

    :param outfit_id: 
    :type outfit_id: str
    :type outfit_id: str

    :rtype: Union[Outfit, Tuple[Outfit, int], Tuple[Outfit, int, Dict[str, str]]
    """
    return 'do some magic!'


def outfits_outfit_id_put(outfit_id, outfit):  # noqa: E501
    """Update an outfit

    Update an existing outfit. # noqa: E501

    :param outfit_id: 
    :type outfit_id: str
    :type outfit_id: str
    :param outfit: 
    :type outfit: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        outfit = Outfit.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def outfits_post(outfit):  # noqa: E501
    """Add a new outfit

    Create a new outfit from wardrobe items. # noqa: E501

    :param outfit: 
    :type outfit: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        outfit = Outfit.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
