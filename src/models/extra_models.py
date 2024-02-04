# coding: utf-8

from pydantic import UUID4, BaseModel

class TokenModel(BaseModel):
    """Defines a token model."""
    user_id: str
