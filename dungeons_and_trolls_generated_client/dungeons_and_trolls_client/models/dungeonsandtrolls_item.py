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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, conlist
from dungeons_and_trolls_client.models.dungeonsandtrolls_attributes import DungeonsandtrollsAttributes
from dungeons_and_trolls_client.models.dungeonsandtrolls_item_type import DungeonsandtrollsItemType

class DungeonsandtrollsItem(BaseModel):
    """
    DungeonsandtrollsItem
    """
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    slot: Optional[DungeonsandtrollsItemType] = None
    price: Optional[StrictInt] = None
    requirements: Optional[DungeonsandtrollsAttributes] = None
    attributes: Optional[DungeonsandtrollsAttributes] = None
    skills: Optional[conlist(DungeonsandtrollsSkill)] = None
    icon: Optional[StrictStr] = None
    unidentified: Optional[StrictBool] = None
    __properties = ["id", "name", "slot", "price", "requirements", "attributes", "skills", "icon", "unidentified"]

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
    def from_json(cls, json_str: str) -> DungeonsandtrollsItem:
        """Create an instance of DungeonsandtrollsItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of requirements
        if self.requirements:
            _dict['requirements'] = self.requirements.to_dict()
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in skills (list)
        _items = []
        if self.skills:
            for _item in self.skills:
                if _item:
                    _items.append(_item.to_dict())
            _dict['skills'] = _items
        # set to None if unidentified (nullable) is None
        # and __fields_set__ contains the field
        if self.unidentified is None and "unidentified" in self.__fields_set__:
            _dict['unidentified'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DungeonsandtrollsItem:
        """Create an instance of DungeonsandtrollsItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DungeonsandtrollsItem.parse_obj(obj)

        _obj = DungeonsandtrollsItem.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "slot": obj.get("slot"),
            "price": obj.get("price"),
            "requirements": DungeonsandtrollsAttributes.from_dict(obj.get("requirements")) if obj.get("requirements") is not None else None,
            "attributes": DungeonsandtrollsAttributes.from_dict(obj.get("attributes")) if obj.get("attributes") is not None else None,
            "skills": [DungeonsandtrollsSkill.from_dict(_item) for _item in obj.get("skills")] if obj.get("skills") is not None else None,
            "icon": obj.get("icon"),
            "unidentified": obj.get("unidentified")
        })
        return _obj

from dungeons_and_trolls_client.models.dungeonsandtrolls_skill import DungeonsandtrollsSkill
DungeonsandtrollsItem.update_forward_refs()

