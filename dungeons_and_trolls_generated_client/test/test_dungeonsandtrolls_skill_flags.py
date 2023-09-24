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

from dungeons_and_trolls_client.models.dungeonsandtrolls_skill_flags import DungeonsandtrollsSkillFlags  # noqa: E501

class TestDungeonsandtrollsSkillFlags(unittest.TestCase):
    """DungeonsandtrollsSkillFlags unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DungeonsandtrollsSkillFlags:
        """Test DungeonsandtrollsSkillFlags
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DungeonsandtrollsSkillFlags`
        """
        model = DungeonsandtrollsSkillFlags()  # noqa: E501
        if include_optional:
            return DungeonsandtrollsSkillFlags(
                requires_alone = True,
                requires_line_of_sight = True,
                allow_target_self = True,
                movement = True,
                knockback = True,
                stun = True,
                ground_effect = True,
                passive = True
            )
        else:
            return DungeonsandtrollsSkillFlags(
        )
        """

    def testDungeonsandtrollsSkillFlags(self):
        """Test DungeonsandtrollsSkillFlags"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
