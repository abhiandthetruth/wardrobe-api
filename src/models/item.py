# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
import uuid
from typing import Any, Dict, List, Optional, Union  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator, UUID4  # noqa: F401
from models.accessory import Accessory
from models.bottomwear import Bottomwear
from models.footwear import Footwear
from models.single_piece import SinglePiece
from models.topwear import Topwear
from models.occasion import Occasion
from models.season import Season
from models.time import Time
from models.underwear import Underwear
from models.color import Color
from models.kind import Kind
from models.material import Material
from models.size import Size

class Item(BaseModel):
    item_id: UUID4 = Field(alias="item_id", Literal=True, default_factory=uuid.uuid4)
    name: Optional[str] = Field(alias="name", default=None, min_length=3)
    image: Optional[str] = Field(alias="image", default=None)
    kind: Optional[Kind] = Field(alias="kind", default=None) 
    category: Union[Accessory, Bottomwear, Footwear, Topwear, SinglePiece, Underwear] = Field(alias="category", default=None)
    size: Optional[Size] = Field(alias="size", default=None)
    material: Optional[Material] = Field(alias="material", default=None)
    time: Optional[Time] = Field(alias="time", default=None)
    season: Optional[Season] = Field(alias="season", default=None)
    occasion: Optional[Occasion] = Field(alias="occasion", default=None)
    tags: Optional[List[str]] = Field(alias="tags", default=None)
    colors: Optional[List[Color]] = Field(alias="colors", default=None)
    user_id: str = Field(alias="user")

Item.update_forward_refs()
