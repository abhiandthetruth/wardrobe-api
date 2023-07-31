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
from openapi_server.models.auth_login_post_request import AuthLoginPostRequest


router = APIRouter()


@router.post(
    "/auth/login",
    responses={
        200: {"description": "Success"},
        401: {"description": "Unauthorized"},
    },
    tags=["Authentication"],
    summary="Authenticate user",
    response_model_by_alias=True,
)
async def auth_login_post(
    auth_login_post_request: AuthLoginPostRequest = Body(None, description=""),
) -> None:
    """Endpoint for user login and authentication."""
    ...
