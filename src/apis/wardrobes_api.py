# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    HTTPException,
    Header,
    Path,
    Query,
    Request,
    Response,
    Security,
    status,
)
from fastapi.encoders import jsonable_encoder

from models.extra_models import TokenModel  # noqa: F401
from models.wardrobe import Wardrobe
from security_api import get_token_bearerAuth

router = APIRouter()
COLLECTION = "wardrobes"


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
    request: Request,
    token: TokenModel = Depends(get_token_bearerAuth)
) -> List[Wardrobe]:
    """Get a list of all user&#39;s wardrobes."""
    # TODO: filter by user_id fetched from token
    wardrobes = list(request.app.database[COLLECTION].find(
        {"user_id", token.user_id}, {"_id": 0}, limit=5))
    return wardrobes


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
    request: Request,
    wardrobe: Wardrobe = Body(None, description=""),
    token: TokenModel = Depends(get_token_bearerAuth)
) -> None:
    """Create a new wardrobe for the user."""
    wardrobe = jsonable_encoder(wardrobe)
    wardrobe.user_id = token.user_id
    new_wardrobe = request.app.database[COLLECTION].insert_one(wardrobe)
    return request.app.database[COLLECTION].find_one({
        "_id": new_wardrobe.inserted_id
    }, {"_id": 0})


@router.delete(
    "/wardrobes/{wardrobe_id}",
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
    request: Request,
    response: Response,
    wardrobe_id: str = Path(description=""),
    token: TokenModel = Depends(get_token_bearerAuth)
) -> None:
    """Delete an existing wardrobe."""
    delete_result = request.app.database[COLLECTION].delete_one(
        {"wardrobe_id": wardrobe_id, "user_id": token.user_id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Wardrobe with ID {id} not found")


@router.get(
    "/wardrobes/{wardrobe_id}",
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
    request: Request,
    wardrobe_id: str = Path(description=""),
    token: TokenModel = Depends(get_token_bearerAuth)
) -> Wardrobe:
    """Get a specific wardrobe by its ID."""
    if (wardrobe := request.app.database[COLLECTION].find_one({"wardrobe_id": wardrobe_id, "user_id": token.user_id}, {"_id": 0})) is not None:
        return wardrobe

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Wardrobe with ID {wardrobe_id} not found")


@router.put(
    "/wardrobes/{wardrobe_id}",
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
    request: Request,
    wardrobe_id: str = Path(description=""),
    wardrobe: Wardrobe = Body(None, description=""),
    token: TokenModel = Depends(get_token_bearerAuth)
) -> None:
    """Update an existing wardrobe."""
    wardrobe = {k: v for k, v in wardrobe.dict().items() if v is not None}
    wardrobe["wardrobe_id"] = wardrobe_id

    if len(wardrobe) >= 1:
        update_result = request.app.database[COLLECTION].update_one(
            {"wardrobe_id": wardrobe_id}, {"$set": wardrobe}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Wardrobe with ID {wardrobe_id} not found")

    if (
        existing_wardrobe := request.app.database[COLLECTION].find_one({"wardrobe_id": wardrobe_id, "user_id": token.user_id}, {"_id": 0})
    ) is not None:
        return existing_wardrobe

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Wardrobe with ID {wardrobe_id} not found")
