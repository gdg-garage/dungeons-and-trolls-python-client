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
from pydantic import BaseModel, Field
from dungeons_and_trolls_client.models.dungeonsandtrolls_attributes import DungeonsandtrollsAttributes
from dungeons_and_trolls_client.models.dungeonsandtrolls_identifier import DungeonsandtrollsIdentifier
from dungeons_and_trolls_client.models.dungeonsandtrolls_identifiers import DungeonsandtrollsIdentifiers
from dungeons_and_trolls_client.models.dungeonsandtrolls_message import DungeonsandtrollsMessage
from dungeons_and_trolls_client.models.dungeonsandtrolls_position import DungeonsandtrollsPosition
from dungeons_and_trolls_client.models.dungeonsandtrolls_skill_use import DungeonsandtrollsSkillUse

class DungeonsandtrollsCommandsBatch(BaseModel):
    """
    DungeonsandtrollsCommandsBatch
    """
    buy: Optional[DungeonsandtrollsIdentifiers] = None
    pick_up: Optional[DungeonsandtrollsIdentifier] = Field(None, alias="pickUp")
    move: Optional[DungeonsandtrollsPosition] = None
    skill: Optional[DungeonsandtrollsSkillUse] = None
    yell: Optional[DungeonsandtrollsMessage] = None
    assign_skill_points: Optional[DungeonsandtrollsAttributes] = Field(None, alias="assignSkillPoints")
    __properties = ["buy", "pickUp", "move", "skill", "yell", "assignSkillPoints"]

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
    def from_json(cls, json_str: str) -> DungeonsandtrollsCommandsBatch:
        """Create an instance of DungeonsandtrollsCommandsBatch from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of buy
        if self.buy:
            _dict['buy'] = self.buy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pick_up
        if self.pick_up:
            _dict['pickUp'] = self.pick_up.to_dict()
        # override the default output from pydantic by calling `to_dict()` of move
        if self.move:
            _dict['move'] = self.move.to_dict()
        # override the default output from pydantic by calling `to_dict()` of skill
        if self.skill:
            _dict['skill'] = self.skill.to_dict()
        # override the default output from pydantic by calling `to_dict()` of yell
        if self.yell:
            _dict['yell'] = self.yell.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assign_skill_points
        if self.assign_skill_points:
            _dict['assignSkillPoints'] = self.assign_skill_points.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DungeonsandtrollsCommandsBatch:
        """Create an instance of DungeonsandtrollsCommandsBatch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DungeonsandtrollsCommandsBatch.parse_obj(obj)

        _obj = DungeonsandtrollsCommandsBatch.parse_obj({
            "buy": DungeonsandtrollsIdentifiers.from_dict(obj.get("buy")) if obj.get("buy") is not None else None,
            "pick_up": DungeonsandtrollsIdentifier.from_dict(obj.get("pickUp")) if obj.get("pickUp") is not None else None,
            "move": DungeonsandtrollsPosition.from_dict(obj.get("move")) if obj.get("move") is not None else None,
            "skill": DungeonsandtrollsSkillUse.from_dict(obj.get("skill")) if obj.get("skill") is not None else None,
            "yell": DungeonsandtrollsMessage.from_dict(obj.get("yell")) if obj.get("yell") is not None else None,
            "assign_skill_points": DungeonsandtrollsAttributes.from_dict(obj.get("assignSkillPoints")) if obj.get("assignSkillPoints") is not None else None
        })
        return _obj


