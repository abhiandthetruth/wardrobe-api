# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    HTTPException,
    Request,
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
from fastapi.encoders import jsonable_encoder
from pymongo import database
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
    request: Request,
    # token_bearerAuth: TokenModel = Security(
    #     get_token_bearerAuth
    # ),
) -> List[Item]:
    """Get a list of all wardrobe items."""
    items: List[Item] = list(request.app.database["items"].find({}, {"_id": 0}, limit=100))
    return items


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
    request: Request,
    response: Response,
    itemId: str = Path(None, description=""),
    # token_bearerAuth: TokenModel = Security(
    #     get_token_bearerAuth
    # ),
) -> None:
    """Delete a wardrobe item."""
    delete_result = request.app.database["items"].delete_one({"itemId": itemId})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID {itemId} not found")

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
    request: Request,
    itemId: str = Path(None, description=""),
    # token_bearerAuth: TokenModel = Security(
    #     get_token_bearerAuth
    # ),
) -> Item:
    """Get a specific wardrobe item by its ID."""
    if (item := request.app.database["items"].find_one({"itemId": itemId}, {"_id": 0})) is not None:
        return item

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID {itemId} not found")


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
    request: Request,
    itemId: str = Path(None, description=""),
    item: Item = Body(None, description=""),
    # token_bearerAuth: TokenModel = Security(
    #     get_token_bearerAuth
    # ),
) -> None:
    """Update an existing wardrobe item."""
    item = {k: v for k, v in item.dict().items() if v is not None}

    if len(item) >= 1:
        update_result = request.app.database["items"].update_one(
            {"_id": id}, {"$set": item}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID {itemId} not found")

    if (
        existing_item := request.app.database["items"].find_one({"itemId": itemId}, {"_id": 0})
    ) is not None:
        return existing_item

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID {id} not found")


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
    request: Request,
    item: Item = Body(None, description=""),
    # token_bearerAuth: TokenModel = Security(
    #     get_token_bearerAuth
    # ),
) -> None:
    """Create a new wardrobe item."""
    item = jsonable_encoder(item)
    new_item = request.app.database["items"].insert_one(item)
    created_item = request.app.database["items"].find_one(
        {"_id": new_item.inserted_id},
        {'_id': 0}
    )

    return created_item
    ...
