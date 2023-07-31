import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.auth_login_post_request import AuthLoginPostRequest  # noqa: E501
from openapi_server import util


def auth_login_post(auth_login_post_request):  # noqa: E501
    """Authenticate user

    Endpoint for user login and authentication. # noqa: E501

    :param auth_login_post_request: 
    :type auth_login_post_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        auth_login_post_request = AuthLoginPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
