# coding: utf-8

"""
    Dungeons and Trolls

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from dungeons_and_trolls_client.models.dungeonsandtrolls_identifiers import DungeonsandtrollsIdentifiers  # noqa: E501

class TestDungeonsandtrollsIdentifiers(unittest.TestCase):
    """DungeonsandtrollsIdentifiers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DungeonsandtrollsIdentifiers:
        """Test DungeonsandtrollsIdentifiers
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DungeonsandtrollsIdentifiers`
        """
        model = DungeonsandtrollsIdentifiers()  # noqa: E501
        if include_optional:
            return DungeonsandtrollsIdentifiers(
                ids = [
                    ''
                    ]
            )
        else:
            return DungeonsandtrollsIdentifiers(
        )
        """

    def testDungeonsandtrollsIdentifiers(self):
        """Test DungeonsandtrollsIdentifiers"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
