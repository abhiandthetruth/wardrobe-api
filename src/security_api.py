# coding: utf-8

import string
from typing import List

from fastapi import Depends, Security  # noqa: F401
from fastapi.openapi.models import OAuthFlowImplicit, OAuthFlows  # noqa: F401
from fastapi.security import (  # noqa: F401
    HTTPAuthorizationCredentials,
    HTTPBasic,
    HTTPBasicCredentials,
    HTTPBearer,
    OAuth2,
    OAuth2AuthorizationCodeBearer,
    OAuth2PasswordBearer,
    SecurityScopes,
)
from fastapi.security.api_key import APIKeyCookie, APIKeyHeader, APIKeyQuery  # noqa: F401
from jose import jwt
from passlib.context import CryptContext
from models.extra_models import TokenModel
from dotenv import dotenv_values
from passlib.exc import UnknownHashError
from fastapi.logger import logger

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
    logger.warning("Hashing password=%s", password)
    hashed_password: str = pwd_context.hash(password)
    logger.warning("Hashed password=%s hash=%s", password, hashed_password)
    return hashed_password

def verify_password_hash(password: string, password_hash: string):
    logger.warning("Trying to verify hash=%s with password=%s", password_hash, password)
    try:
        pwd_context.verify(password, password_hash)
    except UnknownHashError as e:
        logger.warning("Hash not matched %s", e.message)
        return False
    return True