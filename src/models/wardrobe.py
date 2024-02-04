# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional
from uuid import uuid4  # noqa: F401

from pydantic import UUID4, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class Wardrobe(BaseModel):
    wardrobe_id: UUID4 = Field(
        alias="wardrobe_id", default_factory=uuid4, Literal=True)
    name: str = Field(alias="name", default=None)
    location: str = Field(alias="location", default=None)
    user_id: Optional[UUID4] = Field(alias="user")


Wardrobe.model_rebuild()
