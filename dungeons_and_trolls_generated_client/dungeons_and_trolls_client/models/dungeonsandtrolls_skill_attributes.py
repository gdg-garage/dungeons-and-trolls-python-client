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


from typing import Optional
from pydantic import BaseModel, Field
from dungeons_and_trolls_client.models.dungeonsandtrolls_attributes import DungeonsandtrollsAttributes

class DungeonsandtrollsSkillAttributes(BaseModel):
    """
    DungeonsandtrollsSkillAttributes
    """
    strength: Optional[DungeonsandtrollsAttributes] = None
    dexterity: Optional[DungeonsandtrollsAttributes] = None
    intelligence: Optional[DungeonsandtrollsAttributes] = None
    willpower: Optional[DungeonsandtrollsAttributes] = None
    constitution: Optional[DungeonsandtrollsAttributes] = None
    slash_resist: Optional[DungeonsandtrollsAttributes] = Field(None, alias="slashResist")
    pierce_resist: Optional[DungeonsandtrollsAttributes] = Field(None, alias="pierceResist")
    fire_resist: Optional[DungeonsandtrollsAttributes] = Field(None, alias="fireResist")
    poison_resist: Optional[DungeonsandtrollsAttributes] = Field(None, alias="poisonResist")
    electric_resist: Optional[DungeonsandtrollsAttributes] = Field(None, alias="electricResist")
    life: Optional[DungeonsandtrollsAttributes] = None
    stamina: Optional[DungeonsandtrollsAttributes] = None
    mana: Optional[DungeonsandtrollsAttributes] = None
    constant: Optional[DungeonsandtrollsAttributes] = None
    __properties = ["strength", "dexterity", "intelligence", "willpower", "constitution", "slashResist", "pierceResist", "fireResist", "poisonResist", "electricResist", "life", "stamina", "mana", "constant"]

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
    def from_json(cls, json_str: str) -> DungeonsandtrollsSkillAttributes:
        """Create an instance of DungeonsandtrollsSkillAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of strength
        if self.strength:
            _dict['strength'] = self.strength.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dexterity
        if self.dexterity:
            _dict['dexterity'] = self.dexterity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of intelligence
        if self.intelligence:
            _dict['intelligence'] = self.intelligence.to_dict()
        # override the default output from pydantic by calling `to_dict()` of willpower
        if self.willpower:
            _dict['willpower'] = self.willpower.to_dict()
        # override the default output from pydantic by calling `to_dict()` of constitution
        if self.constitution:
            _dict['constitution'] = self.constitution.to_dict()
        # override the default output from pydantic by calling `to_dict()` of slash_resist
        if self.slash_resist:
            _dict['slashResist'] = self.slash_resist.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pierce_resist
        if self.pierce_resist:
            _dict['pierceResist'] = self.pierce_resist.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fire_resist
        if self.fire_resist:
            _dict['fireResist'] = self.fire_resist.to_dict()
        # override the default output from pydantic by calling `to_dict()` of poison_resist
        if self.poison_resist:
            _dict['poisonResist'] = self.poison_resist.to_dict()
        # override the default output from pydantic by calling `to_dict()` of electric_resist
        if self.electric_resist:
            _dict['electricResist'] = self.electric_resist.to_dict()
        # override the default output from pydantic by calling `to_dict()` of life
        if self.life:
            _dict['life'] = self.life.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stamina
        if self.stamina:
            _dict['stamina'] = self.stamina.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mana
        if self.mana:
            _dict['mana'] = self.mana.to_dict()
        # override the default output from pydantic by calling `to_dict()` of constant
        if self.constant:
            _dict['constant'] = self.constant.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DungeonsandtrollsSkillAttributes:
        """Create an instance of DungeonsandtrollsSkillAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DungeonsandtrollsSkillAttributes.parse_obj(obj)

        _obj = DungeonsandtrollsSkillAttributes.parse_obj({
            "strength": DungeonsandtrollsAttributes.from_dict(obj.get("strength")) if obj.get("strength") is not None else None,
            "dexterity": DungeonsandtrollsAttributes.from_dict(obj.get("dexterity")) if obj.get("dexterity") is not None else None,
            "intelligence": DungeonsandtrollsAttributes.from_dict(obj.get("intelligence")) if obj.get("intelligence") is not None else None,
            "willpower": DungeonsandtrollsAttributes.from_dict(obj.get("willpower")) if obj.get("willpower") is not None else None,
            "constitution": DungeonsandtrollsAttributes.from_dict(obj.get("constitution")) if obj.get("constitution") is not None else None,
            "slash_resist": DungeonsandtrollsAttributes.from_dict(obj.get("slashResist")) if obj.get("slashResist") is not None else None,
            "pierce_resist": DungeonsandtrollsAttributes.from_dict(obj.get("pierceResist")) if obj.get("pierceResist") is not None else None,
            "fire_resist": DungeonsandtrollsAttributes.from_dict(obj.get("fireResist")) if obj.get("fireResist") is not None else None,
            "poison_resist": DungeonsandtrollsAttributes.from_dict(obj.get("poisonResist")) if obj.get("poisonResist") is not None else None,
            "electric_resist": DungeonsandtrollsAttributes.from_dict(obj.get("electricResist")) if obj.get("electricResist") is not None else None,
            "life": DungeonsandtrollsAttributes.from_dict(obj.get("life")) if obj.get("life") is not None else None,
            "stamina": DungeonsandtrollsAttributes.from_dict(obj.get("stamina")) if obj.get("stamina") is not None else None,
            "mana": DungeonsandtrollsAttributes.from_dict(obj.get("mana")) if obj.get("mana") is not None else None,
            "constant": DungeonsandtrollsAttributes.from_dict(obj.get("constant")) if obj.get("constant") is not None else None
        })
        return _obj


