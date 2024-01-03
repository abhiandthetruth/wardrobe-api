# coding: utf-8

import string

from fastapi import Depends  # noqa: F401
from fastapi.security import (  # noqa: F401
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from jose import jwt
from passlib.context import CryptContext
from models.extra_models import TokenModel
from dotenv import dotenv_values
from passlib.exc import UnknownHashError

bearer_auth = HTTPBearer()
config = dotenv_values('.env')
SECRET_KEY = config["SECRET_KEY"]
ALGORITHM = config["ALGORITHM"]
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_token_bearerAuth(credentials: HTTPAuthorizationCredentials = Depends(bearer_auth)) -> TokenModel:
    """
    Check and retrieve authentication information from custom bearer token.

    :param credentials Credentials provided by Authorization header
    :type credentials: HTTPAuthorizationCredentials
    :return: Decoded token information or None if token is invalid
    :rtype: TokenModel | None
    """
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        tokenModel = TokenModel(**payload)
        return tokenModel
    except Exception as e:
        return

def get_encoded_token(payload: TokenModel):
    return jwt.encode(payload, SECRET_KEY, ALGORITHM)

def get_password_hash(password: string):
    hashed_password: str = pwd_context.hash(password)
    return hashed_password

def verify_password_hash(password: string, password_hash: string):
    try:
        pwd_context.verify(password, password_hash)
    except UnknownHashError as e:
        return False
    return True