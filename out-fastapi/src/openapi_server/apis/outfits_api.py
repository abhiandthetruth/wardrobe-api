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
from openapi_server.models.outfit import Outfit
from openapi_server.security_api import get_token_bearerAuth

router = APIRouter()


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
async def outfits_get(
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> List[Outfit]:
    """Get a list of all created outfits."""
    ...


@router.delete(
    "/outfits/{outfitId}",
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
    outfitId: str = Path(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> None:
    """Delete an existing outfit."""
    ...


@router.get(
    "/outfits/{outfitId}",
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
    outfitId: str = Path(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> Outfit:
    """Get a specific outfit by its ID."""
    ...


@router.put(
    "/outfits/{outfitId}",
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
    outfitId: str = Path(None, description=""),
    outfit: Outfit = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> None:
    """Update an existing outfit."""
    ...


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
    outfit: Outfit = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> None:
    """Create a new outfit from wardrobe items."""
    ...
