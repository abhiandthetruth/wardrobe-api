# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from enum import Enum

class Kind(str, Enum):
    ACCESSORY = "accessory"
    BOTTOMWEAR = "bottomwear"
    TOPWEAR = "topwear"
    FOOTWEAR = "footwear"
    SINGLE_PIECE = "single_piece"
    UNDERWEAR = "underwear"

