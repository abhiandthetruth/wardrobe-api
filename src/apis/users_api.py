from typing import Dict, List

from fastapi import (  # noqa: F401
    APIRouter,
    HTTPException,
    Request,
    Cookie,
    Depends,
    Path,
    Response,
    status,
)
from fastapi.encoders import jsonable_encoder
from pymongo import database
from models.extra_models import TokenModel  # noqa: F401
from models.user import User
from security_api import get_token_bearerAuth

router = APIRouter()


@router.get(
    "/user",
    responses={
        200: {"model": User, "description": "Success"},
        401: {"description": "Unauthorized"},
        404: {"description": "User not found"},
    },
    tags=["Users"],
    summary="Get logged in user",
    response_model_by_alias=True,
)
async def users_user_id_get(
    request: Request,
    token: TokenModel = Depends(get_token_bearerAuth)
) -> None:
    """Get logged in user"""
    user_id = token.user_id
    if (
        user := request.app.database["users"].find_one(
            {"user_id": user_id}, {"_id": 0, "password": 0}
        )
    ) is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with ID {user_id} not found",
    )