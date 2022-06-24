"""
    CryptoAPIs

    Crypto APIs 2.0 is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs 2.0 can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs 2.0 provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: developers@cryptoapis.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import cryptoapis
from cryptoapis.model.get_transaction_details_by_transaction_idri_recipients_inner import GetTransactionDetailsByTransactionIDRIRecipientsInner
from cryptoapis.model.get_transaction_details_by_transaction_idri_senders_inner import GetTransactionDetailsByTransactionIDRISendersInner
from cryptoapis.model.list_confirmed_transactions_by_address_ri_fee import ListConfirmedTransactionsByAddressRIFee
from cryptoapis.model.list_confirmed_transactions_by_address_ribs import ListConfirmedTransactionsByAddressRIBS
globals()['GetTransactionDetailsByTransactionIDRIRecipientsInner'] = GetTransactionDetailsByTransactionIDRIRecipientsInner
globals()['GetTransactionDetailsByTransactionIDRISendersInner'] = GetTransactionDetailsByTransactionIDRISendersInner
globals()['ListConfirmedTransactionsByAddressRIBS'] = ListConfirmedTransactionsByAddressRIBS
globals()['ListConfirmedTransactionsByAddressRIFee'] = ListConfirmedTransactionsByAddressRIFee
from cryptoapis.model.list_confirmed_transactions_by_address_ri import ListConfirmedTransactionsByAddressRI


class TestListConfirmedTransactionsByAddressRI(unittest.TestCase):
    """ListConfirmedTransactionsByAddressRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListConfirmedTransactionsByAddressRI(self):
        """Test ListConfirmedTransactionsByAddressRI"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListConfirmedTransactionsByAddressRI()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
