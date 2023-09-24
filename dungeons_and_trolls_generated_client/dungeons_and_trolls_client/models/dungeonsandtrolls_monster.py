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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from dungeons_and_trolls_client.models.dungeonsandtrolls_attributes import DungeonsandtrollsAttributes
from dungeons_and_trolls_client.models.dungeonsandtrolls_effect import DungeonsandtrollsEffect
from dungeons_and_trolls_client.models.dungeonsandtrolls_simple_item import DungeonsandtrollsSimpleItem

class DungeonsandtrollsMonster(BaseModel):
    """
    DungeonsandtrollsMonster
    """
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    icon: Optional[StrictStr] = None
    items: Optional[conlist(DungeonsandtrollsSimpleItem)] = None
    effects: Optional[conlist(DungeonsandtrollsEffect)] = None
    life_percentage: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="lifePercentage")
    faction: Optional[StrictStr] = None
    attributes: Optional[DungeonsandtrollsAttributes] = None
    equipped_items: Optional[conlist(DungeonsandtrollsItem)] = Field(None, alias="equippedItems")
    score: Optional[Union[StrictFloat, StrictInt]] = None
    algorithm: Optional[StrictStr] = None
    on_death: Optional[conlist(DungeonsandtrollsDroppable)] = Field(None, alias="onDeath")
    __properties = ["id", "name", "icon", "items", "effects", "lifePercentage", "faction", "attributes", "equippedItems", "score", "algorithm", "onDeath"]

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
    def from_json(cls, json_str: str) -> DungeonsandtrollsMonster:
        """Create an instance of DungeonsandtrollsMonster from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in effects (list)
        _items = []
        if self.effects:
            for _item in self.effects:
                if _item:
                    _items.append(_item.to_dict())
            _dict['effects'] = _items
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in equipped_items (list)
        _items = []
        if self.equipped_items:
            for _item in self.equipped_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['equippedItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in on_death (list)
        _items = []
        if self.on_death:
            for _item in self.on_death:
                if _item:
                    _items.append(_item.to_dict())
            _dict['onDeath'] = _items
        # set to None if score (nullable) is None
        # and __fields_set__ contains the field
        if self.score is None and "score" in self.__fields_set__:
            _dict['score'] = None

        # set to None if algorithm (nullable) is None
        # and __fields_set__ contains the field
        if self.algorithm is None and "algorithm" in self.__fields_set__:
            _dict['algorithm'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DungeonsandtrollsMonster:
        """Create an instance of DungeonsandtrollsMonster from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DungeonsandtrollsMonster.parse_obj(obj)

        _obj = DungeonsandtrollsMonster.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "icon": obj.get("icon"),
            "items": [DungeonsandtrollsSimpleItem.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None,
            "effects": [DungeonsandtrollsEffect.from_dict(_item) for _item in obj.get("effects")] if obj.get("effects") is not None else None,
            "life_percentage": obj.get("lifePercentage"),
            "faction": obj.get("faction"),
            "attributes": DungeonsandtrollsAttributes.from_dict(obj.get("attributes")) if obj.get("attributes") is not None else None,
            "equipped_items": [DungeonsandtrollsItem.from_dict(_item) for _item in obj.get("equippedItems")] if obj.get("equippedItems") is not None else None,
            "score": obj.get("score"),
            "algorithm": obj.get("algorithm"),
            "on_death": [DungeonsandtrollsDroppable.from_dict(_item) for _item in obj.get("onDeath")] if obj.get("onDeath") is not None else None
        })
        return _obj

from dungeons_and_trolls_client.models.dungeonsandtrolls_droppable import DungeonsandtrollsDroppable
from dungeons_and_trolls_client.models.dungeonsandtrolls_item import DungeonsandtrollsItem
DungeonsandtrollsMonster.update_forward_refs()

