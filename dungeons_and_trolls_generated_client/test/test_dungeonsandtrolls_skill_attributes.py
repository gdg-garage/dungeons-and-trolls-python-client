# coding: utf-8

"""
    Dungeons and Trolls

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from dungeons_and_trolls_client.models.dungeonsandtrolls_skill_attributes import DungeonsandtrollsSkillAttributes  # noqa: E501

class TestDungeonsandtrollsSkillAttributes(unittest.TestCase):
    """DungeonsandtrollsSkillAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DungeonsandtrollsSkillAttributes:
        """Test DungeonsandtrollsSkillAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DungeonsandtrollsSkillAttributes`
        """
        model = DungeonsandtrollsSkillAttributes()  # noqa: E501
        if include_optional:
            return DungeonsandtrollsSkillAttributes(
                strength = dungeons_and_trolls_client.models.dungeonsandtrolls_attributes.dungeonsandtrollsAttributes(
                    dexterity = 1.337, 
                    intelligence = 1.337, 
                    willpower = 1.337, 
                    constitution = 1.337, 
                    slash_resist = 1.337, 
                    pierce_resist = 1.337, 
                    fire_resist = 1.337, 
                    poison_resist = 1.337, 
                    electric_resist = 1.337, 
                    life = 1.337, 
                    stamina = 1.337, 
                    mana = 1.337, 
                    constant = 1.337, ),
                dexterity = dungeons_and_trolls_client.models.dungeonsandtrolls_attributes.dungeonsandtrollsAttributes(
                    strength = 1.337, 
                    intelligence = 1.337, 
                    willpower = 1.337, 
                    constitution = 1.337, 
                    slash_resist = 1.337, 
                    pierce_resist = 1.337, 
                    fire_resist = 1.337, 
                    poison_resist = 1.337, 
                    electric_resist = 1.337, 
                    life = 1.337, 
                    stamina = 1.337, 
                    mana = 1.337, 
                    constant = 1.337, ),
                intelligence = dungeons_and_trolls_client.models.dungeonsandtrolls_attributes.dungeonsandtrollsAttributes(
                    strength = 1.337, 
                    dexterity = 1.337, 
                    willpower = 1.337, 
                    constitution = 1.337, 
                    slash_resist = 1.337, 
                    pierce_resist = 1.337, 
                    fire_resist = 1.337, 
                    poison_resist = 1.337, 
                    electric_resist = 1.337, 
                    life = 1.337, 
                    stamina = 1.337, 
                    mana = 1.337, 
                    constant = 1.337, ),
                willpower = dungeons_and_trolls_client.models.dungeonsandtrolls_attributes.dungeonsandtrollsAttributes(
                    strength = 1.337, 
                    dexterity = 1.337, 
                    intelligence = 1.337, 
                    constitution = 1.337, 
                    slash_resist = 1.337, 
                    pierce_resist = 1.337, 
                    fire_resist = 1.337, 
                    poison_resist = 1.337, 
                    electric_resist = 1.337, 
                    life = 1.337, 
                    stamina = 1.337, 
                    mana = 1.337, 
                    constant = 1.337, ),
                constitution = dungeons_and_trolls_client.models.dungeonsandtrolls_attributes.dungeonsandtrollsAttributes(
                    strength = 1.337, 
                    dexterity = 1.337, 
                    intelligence = 1.337, 
                    willpower = 1.337, 
                    slash_resist = 1.337, 
                    pierce_resist = 1.337, 
                    fire_resist = 1.337, 
                    poison_resist = 1.337, 
                    electric_resist = 1.337, 
                    life = 1.337, 
                    stamina = 1.337, 
                    mana = 1.337, 
                    constant = 1.337, ),
                slash_resist = dungeons_and_trolls_client.models.dungeonsandtrolls_attributes.dungeonsandtrollsAttributes(
                    strength = 1.337, 
                    dexterity = 1.337, 
                    intelligence = 1.337, 
                    willpower = 1.337, 
                    constitution = 1.337, 
                    pierce_resist = 1.337, 
                    fire_resist = 1.337, 
                    poison_resist = 1.337, 
                    electric_resist = 1.337, 
                    life = 1.337, 
                    stamina = 1.337, 
                    mana = 1.337, 
                    constant = 1.337, ),
                pierce_resist = dungeons_and_trolls_client.models.dungeonsandtrolls_attributes.dungeonsandtrollsAttributes(
                    strength = 1.337, 
                    dexterity = 1.337, 
                    intelligence = 1.337, 
                    willpower = 1.337, 
                    constitution = 1.337, 
                    slash_resist = 1.337, 
                    fire_resist = 1.337, 
                    poison_resist = 1.337, 
                    electric_resist = 1.337, 
                    life = 1.337, 
                    stamina = 1.337, 
                    mana = 1.337, 
                    constant = 1.337, ),
                fire_resist = dungeons_and_trolls_client.models.dungeonsandtrolls_attributes.dungeonsandtrollsAttributes(
                    strength = 1.337, 
                    dexterity = 1.337, 
                    intelligence = 1.337, 
                    willpower = 1.337, 
                    constitution = 1.337, 
                    slash_resist = 1.337, 
                    pierce_resist = 1.337, 
                    poison_resist = 1.337, 
                    electric_resist = 1.337, 
                    life = 1.337, 
                    stamina = 1.337, 
                    mana = 1.337, 
                    constant = 1.337, ),
                poison_resist = dungeons_and_trolls_client.models.dungeonsandtrolls_attributes.dungeonsandtrollsAttributes(
                    strength = 1.337, 
                    dexterity = 1.337, 
                    intelligence = 1.337, 
                    willpower = 1.337, 
                    constitution = 1.337, 
                    slash_resist = 1.337, 
                    pierce_resist = 1.337, 
                    fire_resist = 1.337, 
                    electric_resist = 1.337, 
                    life = 1.337, 
                    stamina = 1.337, 
                    mana = 1.337, 
                    constant = 1.337, ),
                electric_resist = dungeons_and_trolls_client.models.dungeonsandtrolls_attributes.dungeonsandtrollsAttributes(
                    strength = 1.337, 
                    dexterity = 1.337, 
                    intelligence = 1.337, 
                    willpower = 1.337, 
                    constitution = 1.337, 
                    slash_resist = 1.337, 
                    pierce_resist = 1.337, 
                    fire_resist = 1.337, 
                    poison_resist = 1.337, 
                    life = 1.337, 
                    stamina = 1.337, 
                    mana = 1.337, 
                    constant = 1.337, ),
                life = dungeons_and_trolls_client.models.dungeonsandtrolls_attributes.dungeonsandtrollsAttributes(
                    strength = 1.337, 
                    dexterity = 1.337, 
                    intelligence = 1.337, 
                    willpower = 1.337, 
                    constitution = 1.337, 
                    slash_resist = 1.337, 
                    pierce_resist = 1.337, 
                    fire_resist = 1.337, 
                    poison_resist = 1.337, 
                    electric_resist = 1.337, 
                    stamina = 1.337, 
                    mana = 1.337, 
                    constant = 1.337, ),
                stamina = dungeons_and_trolls_client.models.dungeonsandtrolls_attributes.dungeonsandtrollsAttributes(
                    strength = 1.337, 
                    dexterity = 1.337, 
                    intelligence = 1.337, 
                    willpower = 1.337, 
                    constitution = 1.337, 
                    slash_resist = 1.337, 
                    pierce_resist = 1.337, 
                    fire_resist = 1.337, 
                    poison_resist = 1.337, 
                    electric_resist = 1.337, 
                    life = 1.337, 
                    mana = 1.337, 
                    constant = 1.337, ),
                mana = dungeons_and_trolls_client.models.dungeonsandtrolls_attributes.dungeonsandtrollsAttributes(
                    strength = 1.337, 
                    dexterity = 1.337, 
                    intelligence = 1.337, 
                    willpower = 1.337, 
                    constitution = 1.337, 
                    slash_resist = 1.337, 
                    pierce_resist = 1.337, 
                    fire_resist = 1.337, 
                    poison_resist = 1.337, 
                    electric_resist = 1.337, 
                    life = 1.337, 
                    stamina = 1.337, 
                    constant = 1.337, ),
                constant = dungeons_and_trolls_client.models.dungeonsandtrolls_attributes.dungeonsandtrollsAttributes(
                    strength = 1.337, 
                    dexterity = 1.337, 
                    intelligence = 1.337, 
                    willpower = 1.337, 
                    constitution = 1.337, 
                    slash_resist = 1.337, 
                    pierce_resist = 1.337, 
                    fire_resist = 1.337, 
                    poison_resist = 1.337, 
                    electric_resist = 1.337, 
                    life = 1.337, 
                    stamina = 1.337, 
                    mana = 1.337, )
            )
        else:
            return DungeonsandtrollsSkillAttributes(
        )
        """

    def testDungeonsandtrollsSkillAttributes(self):
        """Test DungeonsandtrollsSkillAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()