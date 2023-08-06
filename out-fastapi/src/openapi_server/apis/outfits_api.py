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

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.outfit import Outfit
from openapi_server.security_api import get_token_bearerAuth

router = APIRouter()
COLLECTION = "outfits"


@router.get(
    "/outfits",
    responses={
        200: {"model": List[Outfit], "description": "Success"},
        401: {"description": "Unauthorized"},
    },
    tags=["Outfits"],
    summary="Get all outfits",
    response_model_by_alias=True,
)
async def outfits_get(request: Request) -> List[Outfit]:
    """Get a list of all created outfits."""
    # TODO: filter by userId fetched from token
    outfits = list(request.app.database[COLLECTION].find(
        {}, {"_id": 0}, limit=5))
    return outfits


@router.delete(
    "/outfits/{outfit_id}",
    responses={
        204: {"description": "No Content"},
        401: {"description": "Unauthorized"},
        404: {"description": "Outfit not found"},
    },
    tags=["Outfits"],
    summary="Delete an outfit",
    response_model_by_alias=True,
)
async def outfits_outfit_id_delete(
    request: Request,
    response: Response,
    outfit_id: str = Path(None, description="")
) -> None:
    """Delete an existing outfit."""
    delete_result = request.app.database[COLLECTION].delete_one(
        {"outfit_id": outfit_id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Outfit with ID {id} not found")


@router.get(
    "/outfits/{outfit_id}",
    responses={
        200: {"model": Outfit, "description": "Success"},
        401: {"description": "Unauthorized"},
        404: {"description": "Outfit not found"},
    },
    tags=["Outfits"],
    summary="Get an outfit by ID",
    response_model_by_alias=True,
)
async def outfits_outfit_id_get(
    request: Request,
    outfit_id: str = Path(None, description="")
) -> Outfit:
    """Get a specific outfit by its ID."""
    if (outfit := request.app.database[COLLECTION].find_one({"outfit_id": outfit_id}, {"_id": 0})) is not None:
        return outfit

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Wardrobe with ID {outfit_id} not found")


@router.put(
    "/outfits/{outfit_id}",
    responses={
        200: {"description": "Success"},
        401: {"description": "Unauthorized"},
        404: {"description": "Outfit not found"},
    },
    tags=["Outfits"],
    summary="Update an outfit",
    response_model_by_alias=True,
)
async def outfits_outfit_id_put(
    request: Request,
    outfit_id: str = Path(None, description=""),
    outfit: Outfit = Body(None, description="")
) -> None:
    """Update an existing outfit."""
    outfit = {k: v for k, v in outfit.dict().items() if v is not None}
    outfit["outfit_id"] = outfit_id

    if len(outfit) >= 1:
        update_result = request.app.database[COLLECTION].update_one(
            {"outfit_id": outfit_id}, {"$set": outfit}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Outfit with ID {outfit_id} not found")

    if (
        existing_outfit := request.app.database[COLLECTION].find_one({"outfit_id": outfit_id}, {"_id": 0})
    ) is not None:
        return existing_outfit

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Outfit with ID {outfit_id} not found")


@router.post(
    "/outfits",
    responses={
        201: {"description": "Created"},
        401: {"description": "Unauthorized"},
    },
    tags=["Outfits"],
    summary="Add a new outfit",
    response_model_by_alias=True,
)
async def outfits_post(
    request: Request,
    outfit: Outfit = Body(None, description="")
) -> None:
    """Create a new outfit from wardrobe items."""
    outfit = jsonable_encoder(outfit)
    new_outfit = request.app.database[COLLECTION].insert_one(outfit)
    return request.app.database[COLLECTION].find_one({
        "_id": new_outfit.inserted_id
    }, {"_id": 0})
