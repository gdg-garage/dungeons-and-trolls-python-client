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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, conlist
from dungeons_and_trolls_client.models.dungeonsandtrolls_map_objects import DungeonsandtrollsMapObjects

class DungeonsandtrollsLevel(BaseModel):
    """
    DungeonsandtrollsLevel
    """
    level: Optional[StrictInt] = None
    width: Optional[StrictInt] = None
    height: Optional[StrictInt] = None
    free: Optional[conlist(conlist(Dict[str, Any]))] = None
    objects: Optional[conlist(DungeonsandtrollsMapObjects)] = None
    ascii: Optional[conlist(StrictStr)] = None
    __properties = ["level", "width", "height", "free", "objects", "ascii"]

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
    def from_json(cls, json_str: str) -> DungeonsandtrollsLevel:
        """Create an instance of DungeonsandtrollsLevel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item in self.objects:
                if _item:
                    _items.append(_item.to_dict())
            _dict['objects'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DungeonsandtrollsLevel:
        """Create an instance of DungeonsandtrollsLevel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DungeonsandtrollsLevel.parse_obj(obj)

        _obj = DungeonsandtrollsLevel.parse_obj({
            "level": obj.get("level"),
            "width": obj.get("width"),
            "height": obj.get("height"),
            "free": obj.get("free"),
            "objects": [DungeonsandtrollsMapObjects.from_dict(_item) for _item in obj.get("objects")] if obj.get("objects") is not None else None,
            "ascii": obj.get("ascii")
        })
        return _obj


