# coding: utf-8

"""
    Dungeons and Trolls

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, conlist
from dungeons_and_trolls_client.models.dungeonsandtrolls_position import DungeonsandtrollsPosition

class DungeonsandtrollsKey(BaseModel):
    """
    DungeonsandtrollsKey
    """
    doors: Optional[conlist(DungeonsandtrollsPosition)] = None
    __properties = ["doors"]

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
    def from_json(cls, json_str: str) -> DungeonsandtrollsKey:
        """Create an instance of DungeonsandtrollsKey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in doors (list)
        _items = []
        if self.doors:
            for _item in self.doors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['doors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DungeonsandtrollsKey:
        """Create an instance of DungeonsandtrollsKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DungeonsandtrollsKey.parse_obj(obj)

        _obj = DungeonsandtrollsKey.parse_obj({
            "doors": [DungeonsandtrollsPosition.from_dict(_item) for _item in obj.get("doors")] if obj.get("doors") is not None else None
        })
        return _obj


