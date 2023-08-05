# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class Wardrobe(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Wardrobe - a model defined in OpenAPI

        name: The name of this Wardrobe [Optional].
        location: The location of this Wardrobe [Optional].
        items: The items of this Wardrobe [Optional].
    """

    name: Optional[str] = Field(alias="name", default=None)
    location: Optional[str] = Field(alias="location", default=None)
    items: Optional[List[str]] = Field(alias="items", default=None)

Wardrobe.update_forward_refs()