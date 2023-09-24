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

from dungeons_and_trolls_client.models.dungeonsandtrolls_commands_batch import DungeonsandtrollsCommandsBatch  # noqa: E501

class TestDungeonsandtrollsCommandsBatch(unittest.TestCase):
    """DungeonsandtrollsCommandsBatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DungeonsandtrollsCommandsBatch:
        """Test DungeonsandtrollsCommandsBatch
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DungeonsandtrollsCommandsBatch`
        """
        model = DungeonsandtrollsCommandsBatch()  # noqa: E501
        if include_optional:
            return DungeonsandtrollsCommandsBatch(
                buy = dungeons_and_trolls_client.models.dungeonsandtrolls_identifiers.dungeonsandtrollsIdentifiers(
                    ids = [
                        ''
                        ], ),
                pick_up = dungeons_and_trolls_client.models.dungeonsandtrolls_identifier.dungeonsandtrollsIdentifier(
                    id = '', ),
                move = dungeons_and_trolls_client.models.dungeonsandtrolls_position.dungeonsandtrollsPosition(
                    position_x = 56, 
                    position_y = 56, ),
                skill = dungeons_and_trolls_client.models.dungeonsandtrolls_skill_use.dungeonsandtrollsSkillUse(
                    skill_id = '', 
                    target_id = '', 
                    position = dungeons_and_trolls_client.models.dungeonsandtrolls_position.dungeonsandtrollsPosition(
                        position_x = 56, 
                        position_y = 56, ), ),
                yell = dungeons_and_trolls_client.models.dungeonsandtrolls_message.dungeonsandtrollsMessage(
                    text = '', ),
                assign_skill_points = dungeons_and_trolls_client.models.dungeonsandtrolls_attributes.dungeonsandtrollsAttributes(
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
                    mana = 1.337, 
                    constant = 1.337, )
            )
        else:
            return DungeonsandtrollsCommandsBatch(
        )
        """

    def testDungeonsandtrollsCommandsBatch(self):
        """Test DungeonsandtrollsCommandsBatch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()