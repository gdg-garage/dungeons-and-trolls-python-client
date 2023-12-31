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
from pydantic import BaseModel, Field, StrictBool, conlist
from dungeons_and_trolls_client.models.dungeonsandtrolls_character import DungeonsandtrollsCharacter
from dungeons_and_trolls_client.models.dungeonsandtrolls_decoration import DungeonsandtrollsDecoration
from dungeons_and_trolls_client.models.dungeonsandtrolls_effect import DungeonsandtrollsEffect
from dungeons_and_trolls_client.models.dungeonsandtrolls_item import DungeonsandtrollsItem
from dungeons_and_trolls_client.models.dungeonsandtrolls_monster import DungeonsandtrollsMonster
from dungeons_and_trolls_client.models.dungeonsandtrolls_position import DungeonsandtrollsPosition
from dungeons_and_trolls_client.models.dungeonsandtrolls_waypoint import DungeonsandtrollsWaypoint

class DungeonsandtrollsMapObjects(BaseModel):
    """
    DungeonsandtrollsMapObjects
    """
    position: Optional[DungeonsandtrollsPosition] = None
    monsters: Optional[conlist(DungeonsandtrollsMonster)] = None
    players: Optional[conlist(DungeonsandtrollsCharacter)] = None
    is_stairs: Optional[StrictBool] = Field(None, alias="isStairs")
    portal: Optional[DungeonsandtrollsWaypoint] = None
    decorations: Optional[conlist(DungeonsandtrollsDecoration)] = None
    effects: Optional[conlist(DungeonsandtrollsEffect)] = None
    items: Optional[conlist(DungeonsandtrollsItem)] = None
    is_free: Optional[StrictBool] = Field(None, alias="isFree")
    is_wall: Optional[StrictBool] = Field(None, alias="isWall")
    is_door: Optional[StrictBool] = Field(None, alias="isDoor")
    is_spawn: Optional[StrictBool] = Field(None, alias="isSpawn")
    __properties = ["position", "monsters", "players", "isStairs", "portal", "decorations", "effects", "items", "isFree", "isWall", "isDoor", "isSpawn"]

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
    def from_json(cls, json_str: str) -> DungeonsandtrollsMapObjects:
        """Create an instance of DungeonsandtrollsMapObjects from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of position
        if self.position:
            _dict['position'] = self.position.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in monsters (list)
        _items = []
        if self.monsters:
            for _item in self.monsters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['monsters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in players (list)
        _items = []
        if self.players:
            for _item in self.players:
                if _item:
                    _items.append(_item.to_dict())
            _dict['players'] = _items
        # override the default output from pydantic by calling `to_dict()` of portal
        if self.portal:
            _dict['portal'] = self.portal.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in decorations (list)
        _items = []
        if self.decorations:
            for _item in self.decorations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['decorations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in effects (list)
        _items = []
        if self.effects:
            for _item in self.effects:
                if _item:
                    _items.append(_item.to_dict())
            _dict['effects'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # set to None if is_spawn (nullable) is None
        # and __fields_set__ contains the field
        if self.is_spawn is None and "is_spawn" in self.__fields_set__:
            _dict['isSpawn'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DungeonsandtrollsMapObjects:
        """Create an instance of DungeonsandtrollsMapObjects from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DungeonsandtrollsMapObjects.parse_obj(obj)

        _obj = DungeonsandtrollsMapObjects.parse_obj({
            "position": DungeonsandtrollsPosition.from_dict(obj.get("position")) if obj.get("position") is not None else None,
            "monsters": [DungeonsandtrollsMonster.from_dict(_item) for _item in obj.get("monsters")] if obj.get("monsters") is not None else None,
            "players": [DungeonsandtrollsCharacter.from_dict(_item) for _item in obj.get("players")] if obj.get("players") is not None else None,
            "is_stairs": obj.get("isStairs"),
            "portal": DungeonsandtrollsWaypoint.from_dict(obj.get("portal")) if obj.get("portal") is not None else None,
            "decorations": [DungeonsandtrollsDecoration.from_dict(_item) for _item in obj.get("decorations")] if obj.get("decorations") is not None else None,
            "effects": [DungeonsandtrollsEffect.from_dict(_item) for _item in obj.get("effects")] if obj.get("effects") is not None else None,
            "items": [DungeonsandtrollsItem.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None,
            "is_free": obj.get("isFree"),
            "is_wall": obj.get("isWall"),
            "is_door": obj.get("isDoor"),
            "is_spawn": obj.get("isSpawn")
        })
        return _obj


