# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class AuthLoginPostRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AuthLoginPostRequest - a model defined in OpenAPI

        email_id: The email_id of this AuthLoginPostRequest [Optional].
        password: The password of this AuthLoginPostRequest [Optional].
    """

    email_id: Optional[EmailStr] = Field(alias="email_id", default=None)
    password: Optional[str] = Field(alias="password", default=None)

AuthLoginPostRequest.update_forward_refs()
