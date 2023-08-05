# coding: utf-8

from __future__ import annotations
from datetime import date, datetime
from enum import Enum  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class Season(str, Enum):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Season - a model defined in OpenAPI

    """
    SUMMER = "summer"
    WINTER = "winter"
    SPRING = "spring"
    MONSOON = "monsoon"


