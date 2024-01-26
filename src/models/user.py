# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Literal, Optional
import uuid  # noqa: F401

from pydantic import UUID4, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class User(BaseModel):
    user_id: UUID4 = Field(alias="user_id", Literal=True, default_factory=uuid.uuid4)
    name: str = Field(alias="name", default=None)
    image: Optional[str] = Field(alias="image", default=None)
    email_id: EmailStr = Field(alias="email_id", default=None)
    password: str = Field(alias="password", default=None)
    connections: Optional[List[UUID4]] = Field(alias="connections", default=None)

User.update_forward_refs()
