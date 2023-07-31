import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.connections_add_post_request import ConnectionsAddPostRequest  # noqa: E501
from openapi_server import util


def connections_add_post(connections_add_post_request):  # noqa: E501
    """Add a connection between users

    Create a connection between the current user and another user. # noqa: E501

    :param connections_add_post_request: 
    :type connections_add_post_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        connections_add_post_request = ConnectionsAddPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
