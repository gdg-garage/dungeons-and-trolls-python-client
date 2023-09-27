# coding: utf-8

"""
    Dungeons and Trolls

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class DungeonsandtrollsEventType(str, Enum):
    """
    DungeonsandtrollsEventType
    """

    """
    allowed enum values
    """
    DAMAGE = 'DAMAGE'
    MESSAGE = 'MESSAGE'
    BUY = 'BUY'
    EQUIP = 'EQUIP'
    ERROR = 'ERROR'
    SKILL = 'SKILL'
    DEATH = 'DEATH'
    SCORE = 'SCORE'
    MOVE = 'MOVE'

    @classmethod
    def from_json(cls, json_str: str) -> DungeonsandtrollsEventType:
        """Create an instance of DungeonsandtrollsEventType from a JSON string"""
        return DungeonsandtrollsEventType(json.loads(json_str))


