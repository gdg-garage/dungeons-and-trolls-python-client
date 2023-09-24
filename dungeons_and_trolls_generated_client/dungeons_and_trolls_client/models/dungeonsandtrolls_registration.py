# coding: utf-8

"""
    Dungeons and Trolls

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class DungeonsandtrollsRegistration(BaseModel):
    """
    DungeonsandtrollsRegistration
    """
    api_key: Optional[StrictStr] = Field(None, alias="apiKey")
    __properties = ["apiKey"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DungeonsandtrollsRegistration:
        """Create an instance of DungeonsandtrollsRegistration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if api_key (nullable) is None
        # and __fields_set__ contains the field
        if self.api_key is None and "api_key" in self.__fields_set__:
            _dict['apiKey'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DungeonsandtrollsRegistration:
        """Create an instance of DungeonsandtrollsRegistration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DungeonsandtrollsRegistration.parse_obj(obj)

        _obj = DungeonsandtrollsRegistration.parse_obj({
            "api_key": obj.get("apiKey")
        })
        return _obj


