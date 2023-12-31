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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, conlist
from dungeons_and_trolls_client.models.dungeonsandtrolls_character import DungeonsandtrollsCharacter
from dungeons_and_trolls_client.models.dungeonsandtrolls_event import DungeonsandtrollsEvent
from dungeons_and_trolls_client.models.dungeonsandtrolls_item import DungeonsandtrollsItem
from dungeons_and_trolls_client.models.dungeonsandtrolls_map import DungeonsandtrollsMap
from dungeons_and_trolls_client.models.dungeonsandtrolls_position import DungeonsandtrollsPosition

class DungeonsandtrollsGameState(BaseModel):
    """
    DungeonsandtrollsGameState
    """
    map: Optional[DungeonsandtrollsMap] = None
    shop_items: Optional[conlist(DungeonsandtrollsItem)] = Field(None, alias="shopItems")
    character: Optional[DungeonsandtrollsCharacter] = None
    current_position: Optional[DungeonsandtrollsPosition] = Field(None, alias="currentPosition")
    current_level: Optional[StrictInt] = Field(None, alias="currentLevel")
    tick: Optional[StrictInt] = None
    events: Optional[conlist(DungeonsandtrollsEvent)] = Field(None, description="List of events which occurred in the previous tick. Useful for visualising effects, debugging and communication.")
    score: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["map", "shopItems", "character", "currentPosition", "currentLevel", "tick", "events", "score"]

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
    def from_json(cls, json_str: str) -> DungeonsandtrollsGameState:
        """Create an instance of DungeonsandtrollsGameState from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of map
        if self.map:
            _dict['map'] = self.map.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in shop_items (list)
        _items = []
        if self.shop_items:
            for _item in self.shop_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['shopItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of character
        if self.character:
            _dict['character'] = self.character.to_dict()
        # override the default output from pydantic by calling `to_dict()` of current_position
        if self.current_position:
            _dict['currentPosition'] = self.current_position.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in events (list)
        _items = []
        if self.events:
            for _item in self.events:
                if _item:
                    _items.append(_item.to_dict())
            _dict['events'] = _items
        # set to None if current_level (nullable) is None
        # and __fields_set__ contains the field
        if self.current_level is None and "current_level" in self.__fields_set__:
            _dict['currentLevel'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DungeonsandtrollsGameState:
        """Create an instance of DungeonsandtrollsGameState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DungeonsandtrollsGameState.parse_obj(obj)

        _obj = DungeonsandtrollsGameState.parse_obj({
            "map": DungeonsandtrollsMap.from_dict(obj.get("map")) if obj.get("map") is not None else None,
            "shop_items": [DungeonsandtrollsItem.from_dict(_item) for _item in obj.get("shopItems")] if obj.get("shopItems") is not None else None,
            "character": DungeonsandtrollsCharacter.from_dict(obj.get("character")) if obj.get("character") is not None else None,
            "current_position": DungeonsandtrollsPosition.from_dict(obj.get("currentPosition")) if obj.get("currentPosition") is not None else None,
            "current_level": obj.get("currentLevel"),
            "tick": obj.get("tick"),
            "events": [DungeonsandtrollsEvent.from_dict(_item) for _item in obj.get("events")] if obj.get("events") is not None else None,
            "score": obj.get("score")
        })
        return _obj


