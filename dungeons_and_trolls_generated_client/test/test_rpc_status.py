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

from dungeons_and_trolls_client.models.rpc_status import RpcStatus  # noqa: E501

class TestRpcStatus(unittest.TestCase):
    """RpcStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RpcStatus:
        """Test RpcStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RpcStatus`
        """
        model = RpcStatus()  # noqa: E501
        if include_optional:
            return RpcStatus(
                code = 56,
                message = '',
                details = [
                    {
                        'key' : None
                        }
                    ]
            )
        else:
            return RpcStatus(
        )
        """

    def testRpcStatus(self):
        """Test RpcStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
