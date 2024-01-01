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
from jose import jwt
from models.extra_models import TokenModel  # noqa: F401
from models.auth_login_post_request import AuthLoginPostRequest
from models.auth_register_post_request import AuthRegisterPostRequest
from models.user import User
from security_api import (
    get_encoded_token,
    get_password_hash,
)

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
    request: Request,
    response: Response,
    auth_login_post_request: AuthLoginPostRequest = Body(None, description=""),
) -> None:
    """Endpoint for user login and authentication."""
    email_id = auth_login_post_request.email_id
    user: User
    if (
        user := request.app.database["users"].find_one(
            {
                "email_id": email_id,
                "password": get_password_hash(auth_login_post_request.password),
            },
            {"_id": 0},
        )
    ) is not None:
        response.headers["X-Auth-Token"] = get_encoded_token({"user_id": user.user_id})
        response.status_code = 204
        return response

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with ID {email_id} not found",
    )


@router.post(
    "/auth/register",
    responses={
        200: {"description": "Success"},
        401: {"description": "Unauthorized"},
    },
    tags=["Authentication"],
    summary="Register user",
    response_model_by_alias=True,
)
async def auth_register_post(
    request: Request,
    auth_register_post_request: AuthRegisterPostRequest = Body(None, description=""),
) -> None:
    """Endpoint for user registration."""
    name, email_id, password = (
        auth_register_post_request.name,
        auth_register_post_request.email_id,
        auth_register_post_request.password,
    )
    user = jsonable_encoder(
        User(
            name=name,
            email_id=email_id,
            password=get_password_hash(password),
        )
    )
    new_user = request.app.database["users"].insert_one(user)
    created_user = request.app.database["users"].find_one(
        {"_id": new_user.inserted_id}, {"_id": 0, "password": 0}
    )
    return created_user
