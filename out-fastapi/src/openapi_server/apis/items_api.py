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
from openapi_server.models.item import Item
from openapi_server.security_api import get_token_bearerAuth

router = APIRouter()


@router.get(
    "/items",
    responses={
        200: {"model": List[Item], "description": "Success"},
        401: {"description": "Unauthorized"},
    },
    tags=["Items"],
    summary="Get all items",
    response_model_by_alias=True,
)
async def items_get(
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> List[Item]:
    """Get a list of all wardrobe items."""
    ...


@router.delete(
    "/items/{itemId}",
    responses={
        204: {"description": "No Content"},
        401: {"description": "Unauthorized"},
        404: {"description": "Item not found"},
    },
    tags=["Items"],
    summary="Delete an item",
    response_model_by_alias=True,
)
async def items_item_id_delete(
    itemId: str = Path(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> None:
    """Delete a wardrobe item."""
    ...


@router.get(
    "/items/{itemId}",
    responses={
        200: {"model": Item, "description": "Success"},
        401: {"description": "Unauthorized"},
        404: {"description": "Item not found"},
    },
    tags=["Items"],
    summary="Get an item by ID",
    response_model_by_alias=True,
)
async def items_item_id_get(
    itemId: str = Path(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> Item:
    """Get a specific wardrobe item by its ID."""
    ...


@router.put(
    "/items/{itemId}",
    responses={
        200: {"description": "Success"},
        401: {"description": "Unauthorized"},
        404: {"description": "Item not found"},
    },
    tags=["Items"],
    summary="Update an item",
    response_model_by_alias=True,
)
async def items_item_id_put(
    itemId: str = Path(None, description=""),
    item: Item = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> None:
    """Update an existing wardrobe item."""
    ...


@router.post(
    "/items",
    responses={
        201: {"description": "Created"},
        401: {"description": "Unauthorized"},
    },
    tags=["Items"],
    summary="Add a new item",
    response_model_by_alias=True,
)
async def items_post(
    item: Item = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> None:
    """Create a new wardrobe item."""
    ...
