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
from openapi_server.models.wardrobe import Wardrobe
from openapi_server.security_api import get_token_bearerAuth

router = APIRouter()


@router.get(
    "/wardrobes",
    responses={
        200: {"model": List[Wardrobe], "description": "Success"},
        401: {"description": "Unauthorized"},
    },
    tags=["Wardrobes"],
    summary="Get all wardrobes",
    response_model_by_alias=True,
)
async def wardrobes_get(
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> List[Wardrobe]:
    """Get a list of all user&#39;s wardrobes."""
    ...


@router.post(
    "/wardrobes",
    responses={
        201: {"description": "Created"},
        401: {"description": "Unauthorized"},
    },
    tags=["Wardrobes"],
    summary="Add a new wardrobe",
    response_model_by_alias=True,
)
async def wardrobes_post(
    wardrobe: Wardrobe = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> None:
    """Create a new wardrobe for the user."""
    ...


@router.delete(
    "/wardrobes/{wardrobeId}",
    responses={
        204: {"description": "No Content"},
        401: {"description": "Unauthorized"},
        404: {"description": "Wardrobe not found"},
    },
    tags=["Wardrobes"],
    summary="Delete a wardrobe",
    response_model_by_alias=True,
)
async def wardrobes_wardrobe_id_delete(
    wardrobeId: str = Path(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> None:
    """Delete an existing wardrobe."""
    ...


@router.get(
    "/wardrobes/{wardrobeId}",
    responses={
        200: {"model": Wardrobe, "description": "Success"},
        401: {"description": "Unauthorized"},
        404: {"description": "Wardrobe not found"},
    },
    tags=["Wardrobes"],
    summary="Get a wardrobe by ID",
    response_model_by_alias=True,
)
async def wardrobes_wardrobe_id_get(
    wardrobeId: str = Path(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> Wardrobe:
    """Get a specific wardrobe by its ID."""
    ...


@router.put(
    "/wardrobes/{wardrobeId}",
    responses={
        200: {"description": "Success"},
        401: {"description": "Unauthorized"},
        404: {"description": "Wardrobe not found"},
    },
    tags=["Wardrobes"],
    summary="Update a wardrobe",
    response_model_by_alias=True,
)
async def wardrobes_wardrobe_id_put(
    wardrobeId: str = Path(None, description=""),
    wardrobe: Wardrobe = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> None:
    """Update an existing wardrobe."""
    ...
