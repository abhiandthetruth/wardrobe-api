# coding: utf-8

import os
import random
from typing import Dict, List
from dotenv import dotenv_values  # noqa: F401
import dropbox

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
    UploadFile,
    status,
)
from fastapi.encoders import jsonable_encoder
from pymongo import database
from models.extra_models import TokenModel  # noqa: F401
from models.item import Item
from security_api import get_token_bearerAuth

router = APIRouter()
config = dotenv_values('.env')
dbx = dropbox.Dropbox(
    app_key=config["DROPBOX_APP_KEY"],
    app_secret=config["DROPBOX_APP_SECRET"],
    oauth2_refresh_token=config["DROPBOX_REFRESH_TOKEN"]
)

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
    request: Request, token: TokenModel = Depends(get_token_bearerAuth)
) -> List[Item]:
    """Get a list of all wardrobe items."""
    items: List[Item] = list(
        request.app.database["items"].find(
            {"user_id": token.user_id}, {"_id": 0}, limit=0
        )
    )
    return items


@router.delete(
    "/items/{item_id}",
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
    item_id: str = Path(description=""),
    token: TokenModel = Depends(get_token_bearerAuth),
) -> None:
    """Delete a wardrobe item."""
    delete_result = request.app.database["items"].delete_one(
        {"item_id": item_id, "user_id": token.user_id}
    )

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with ID {item_id} not found",
    )


@router.get(
    "/items/{item_id}",
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
    item_id: str = Path(description=""),
    token: TokenModel = Depends(get_token_bearerAuth),
) -> Item:
    """Get a specific wardrobe item by its ID."""
    if (
        item := request.app.database["items"].find_one(
            {"item_id": item_id, "user_id": token.user_id}, {"_id": 0}
        )
    ) is not None:
        return item

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with ID {item_id} not found",
    )


@router.put(
    "/items/{item_id}",
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
    item_id: str = Path(description=""),
    item: Item = Body(None, description=""),
    token: TokenModel = Depends(get_token_bearerAuth),
) -> Item:
    """Update an existing wardrobe item."""
    item = {k: v for k, v in item.dict().items() if v is not None and k not in ["user_id", "item_id"]}

    if len(item) >= 1:
        request.app.database["items"].update_one(
            {"item_id": item_id, "user_id": token.user_id}, {"$set": item}
        )

    if (
        existing_item := request.app.database["items"].find_one(
            {"item_id": item_id, "user_id": token.user_id}, {"_id": 0}
        )
    ) is not None:
        return existing_item

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID {id} not found"
    )


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
    token: TokenModel =  Depends(get_token_bearerAuth),
) -> Item:
    """Create a new wardrobe item."""
    print("Found token", token, type(token))
    item = jsonable_encoder(item)
    # TODO: convert this to a dependency once it is needed in wardrobes and outfits
    if token.user_id != item["user_id"]:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Trying to create an item for another user, sneaky!")
    item["user_id"] = token.user_id
    new_item = request.app.database["items"].insert_one(item)
    created_item = request.app.database["items"].find_one(
        {"_id": new_item.inserted_id}, {"_id": 0}
    )
    return created_item

@router.post(
    "/items/{item_id}/images",
    responses={
        201: {"description": "Created"},
        401: {"description": "Unauthorized"},
    },
    tags=["Item Images"],
    summary="Add a new item",
    response_model_by_alias=True,
)
async def items_post(
    request: Request,
    image_file: UploadFile,
    item_id: str = Path(description=""),
    token: TokenModel =  Depends(get_token_bearerAuth),
) -> Item:
    if (
        item := request.app.database["items"].find_one(
            {"item_id": item_id, "user_id": token.user_id}, {"_id": 0}
        )
    ) is not None:
        if token.user_id != item["user_id"]:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Trying to create an item for another user, sneaky!")
        
        # support multiple images for an item with the same name since we don't support deletion of existing images
        image_file_name: str = f"{random.randint(100, 999999)}_{image_file.filename}"
        dropbox_dest_path: str = f"/{item['user_id']}/{item['item_id']}/{image_file_name}"

        dbx.files_upload(await image_file.read(), dropbox_dest_path, autorename=True)
        shareable_url = f"{dbx.sharing_create_shared_link_with_settings(dropbox_dest_path).url}&raw=1"

        item["image"] = shareable_url
        request.app.database["items"].update_one(
            {"item_id": item_id, "user_id": token.user_id}, {"$set": item}
        )

        return item

    print("item not found")
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with ID {item_id} not found",
    )