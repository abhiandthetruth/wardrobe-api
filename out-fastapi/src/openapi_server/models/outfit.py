# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.occasion import Occasion
from openapi_server.models.season import Season
from openapi_server.models.time import Time


class Outfit(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Outfit - a model defined in OpenAPI

        name: The name of this Outfit [Optional].
        time: The time of this Outfit [Optional].
        season: The season of this Outfit [Optional].
        occasion: The occasion of this Outfit [Optional].
        topwears: The topwears of this Outfit [Optional].
        bottomwears: The bottomwears of this Outfit [Optional].
        accessories: The accessories of this Outfit [Optional].
        footwears: The footwears of this Outfit [Optional].
    """

    name: Optional[str] = Field(alias="name", default=None)
    time: Optional[Time] = Field(alias="time", default=None)
    season: Optional[Season] = Field(alias="season", default=None)
    occasion: Optional[Occasion] = Field(alias="occasion", default=None)
    topwears: Optional[List[str]] = Field(alias="topwears", default=None)
    bottomwears: Optional[List[str]] = Field(alias="bottomwears", default=None)
    accessories: Optional[List[str]] = Field(alias="accessories", default=None)
    footwears: Optional[List[str]] = Field(alias="footwears", default=None)

Outfit.update_forward_refs()