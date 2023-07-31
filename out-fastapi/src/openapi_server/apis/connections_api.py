# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.connections_add_post_request import ConnectionsAddPostRequest
from openapi_server.security_api import get_token_bearerAuth

router = APIRouter()


@router.post(
    "/connections/add",
    responses={
        201: {"description": "Created"},
        401: {"description": "Unauthorized"},
    },
    tags=["Connections"],
    summary="Add a connection between users",
    response_model_by_alias=True,
)
async def connections_add_post(
    connections_add_post_request: ConnectionsAddPostRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> None:
    """Create a connection between the current user and another user."""
    ...
