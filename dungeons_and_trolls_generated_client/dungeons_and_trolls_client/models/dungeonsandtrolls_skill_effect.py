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


from typing import List, Optional
from pydantic import BaseModel, conlist
from dungeons_and_trolls_client.models.dungeonsandtrolls_skill_attributes import DungeonsandtrollsSkillAttributes
from dungeons_and_trolls_client.models.dungeonsandtrolls_skill_flags import DungeonsandtrollsSkillFlags

class DungeonsandtrollsSkillEffect(BaseModel):
    """
    DungeonsandtrollsSkillEffect
    """
    attributes: Optional[DungeonsandtrollsSkillAttributes] = None
    flags: Optional[DungeonsandtrollsSkillFlags] = None
    summons: Optional[conlist(DungeonsandtrollsDroppable)] = None
    __properties = ["attributes", "flags", "summons"]

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
    def from_json(cls, json_str: str) -> DungeonsandtrollsSkillEffect:
        """Create an instance of DungeonsandtrollsSkillEffect from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of flags
        if self.flags:
            _dict['flags'] = self.flags.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in summons (list)
        _items = []
        if self.summons:
            for _item in self.summons:
                if _item:
                    _items.append(_item.to_dict())
            _dict['summons'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DungeonsandtrollsSkillEffect:
        """Create an instance of DungeonsandtrollsSkillEffect from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DungeonsandtrollsSkillEffect.parse_obj(obj)

        _obj = DungeonsandtrollsSkillEffect.parse_obj({
            "attributes": DungeonsandtrollsSkillAttributes.from_dict(obj.get("attributes")) if obj.get("attributes") is not None else None,
            "flags": DungeonsandtrollsSkillFlags.from_dict(obj.get("flags")) if obj.get("flags") is not None else None,
            "summons": [DungeonsandtrollsDroppable.from_dict(_item) for _item in obj.get("summons")] if obj.get("summons") is not None else None
        })
        return _obj

from dungeons_and_trolls_client.models.dungeonsandtrolls_droppable import DungeonsandtrollsDroppable
DungeonsandtrollsSkillEffect.update_forward_refs()
