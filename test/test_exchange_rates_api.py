"""
    CryptoAPIs

    Crypto APIs is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2021-03-20
    Contact: developers@cryptoapis.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import cryptoapis
from cryptoapis.api.exchange_rates_api import ExchangeRatesApi  # noqa: E501


class TestExchangeRatesApi(unittest.TestCase):
    """ExchangeRatesApi unit test stubs"""

    def setUp(self):
        self.api = ExchangeRatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_exchange_rate_by_asset_symbols(self):
        """Test case for get_exchange_rate_by_asset_symbols

        Get Exchange Rate By Asset Symbols  # noqa: E501
        """
        pass

    def test_get_exchange_rate_by_assets_ids(self):
        """Test case for get_exchange_rate_by_assets_ids

        Get Exchange Rate By Assets IDs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
