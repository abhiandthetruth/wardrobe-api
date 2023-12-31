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

class Item(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Item - a model defined in OpenAPI

        name: The name of this Item [Optional].
        image: The image of this Item [Optional].
        category: The category of this Item [Optional].
        size: The size of this Item [Optional].
        material: The material of this Item [Optional].
        time: The time of this Item [Optional].
        season: The season of this Item [Optional].
        occasion: The occasion of this Item [Optional].
        tags: The tags of this Item [Optional].
        colors: The colors of this Item [Optional].
    """
    item_id: UUID4 = Field(alias="item_id", Literal=True, default_factory=uuid.uuid4)
    name: Optional[str] = Field(alias="name", default=None, min_length=3)
    image: Optional[str] = Field(alias="image", default=None)
    category: Union[Accessory, Bottomwear, Footwear, Topwear, SinglePiece, Underwear] = Field(alias="category", default=None)
    size: Optional[str] = Field(alias="size", default=None)
    material: Optional[str] = Field(alias="material", default=None)
    time: Optional[Time] = Field(alias="time", default=None)
    season: Optional[Season] = Field(alias="season", default=None)
    occasion: Optional[Occasion] = Field(alias="occasion", default=None)
    tags: Optional[List[str]] = Field(alias="tags", default=None)
    colors: Optional[List[str]] = Field(alias="colors", default=None)
    user_id: str = Field(alias="user")

Item.update_forward_refs()
