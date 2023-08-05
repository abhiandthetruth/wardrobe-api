# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.accessory import Accessory
from openapi_server.models.bottomwear import Bottomwear
from openapi_server.models.footwear import Footwear
from openapi_server.models.single_piece import SinglePiece
from openapi_server.models.topwear import Topwear


class ItemCategory(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ItemCategory - a model defined in OpenAPI

    """


ItemCategory.update_forward_refs()