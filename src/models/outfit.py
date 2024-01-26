# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional
from uuid import uuid4  # noqa: F401

from pydantic import UUID4, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from models.occasion import Occasion
from models.season import Season
from models.time import Time


class Outfit(BaseModel):
    outfit_id: Optional[str] = Field(
        alias="outfit_id", default_factory=uuid4, Literal=True)
    user_id: Optional[UUID4] = Field(alias="user Id")
    name: str = Field(alias="name", default=None)
    time: Optional[Time] = Field(alias="time", default=None)
    season: Optional[Season] = Field(alias="season", default=None)
    occasion: Optional[Occasion] = Field(alias="occasion", default=None)
    topwears: Optional[List[str]] = Field(alias="topwears", default=None)
    bottomwears: Optional[List[str]] = Field(alias="bottomwears", default=None)
    accessories: Optional[List[str]] = Field(alias="accessories", default=None)
    footwears: Optional[List[str]] = Field(alias="footwears", default=None)
    


Outfit.update_forward_refs()
