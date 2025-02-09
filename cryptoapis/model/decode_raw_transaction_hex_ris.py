"""
    CryptoAPIs

    Crypto APIs is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2021-03-20
    Contact: developers@cryptoapis.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cryptoapis.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from cryptoapis.exceptions import ApiAttributeError


def lazy_import():
    from cryptoapis.model.decode_raw_transaction_hex_risb import DecodeRawTransactionHexRISB
    from cryptoapis.model.decode_raw_transaction_hex_risb2 import DecodeRawTransactionHexRISB2
    from cryptoapis.model.decode_raw_transaction_hex_risb22 import DecodeRawTransactionHexRISB22
    from cryptoapis.model.decode_raw_transaction_hex_risd import DecodeRawTransactionHexRISD
    from cryptoapis.model.decode_raw_transaction_hex_risd2 import DecodeRawTransactionHexRISD2
    from cryptoapis.model.decode_raw_transaction_hex_rise import DecodeRawTransactionHexRISE
    from cryptoapis.model.decode_raw_transaction_hex_rise2 import DecodeRawTransactionHexRISE2
    from cryptoapis.model.decode_raw_transaction_hex_risl import DecodeRawTransactionHexRISL
    from cryptoapis.model.decode_raw_transaction_hex_risz import DecodeRawTransactionHexRISZ
    from cryptoapis.model.decode_raw_transaction_hex_risz_vin_inner import DecodeRawTransactionHexRISZVinInner
    from cryptoapis.model.decode_raw_transaction_hex_risz_vout_inner import DecodeRawTransactionHexRISZVoutInner
    globals()['DecodeRawTransactionHexRISB'] = DecodeRawTransactionHexRISB
    globals()['DecodeRawTransactionHexRISB2'] = DecodeRawTransactionHexRISB2
    globals()['DecodeRawTransactionHexRISB22'] = DecodeRawTransactionHexRISB22
    globals()['DecodeRawTransactionHexRISD'] = DecodeRawTransactionHexRISD
    globals()['DecodeRawTransactionHexRISD2'] = DecodeRawTransactionHexRISD2
    globals()['DecodeRawTransactionHexRISE'] = DecodeRawTransactionHexRISE
    globals()['DecodeRawTransactionHexRISE2'] = DecodeRawTransactionHexRISE2
    globals()['DecodeRawTransactionHexRISL'] = DecodeRawTransactionHexRISL
    globals()['DecodeRawTransactionHexRISZ'] = DecodeRawTransactionHexRISZ
    globals()['DecodeRawTransactionHexRISZVinInner'] = DecodeRawTransactionHexRISZVinInner
    globals()['DecodeRawTransactionHexRISZVoutInner'] = DecodeRawTransactionHexRISZVoutInner


class DecodeRawTransactionHexRIS(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'weight': (int,),  # noqa: E501
            'approximate_fee': (str,),  # noqa: E501
            'approximate_minimum_required_fee': (str,),  # noqa: E501
            'gas_paid_for_data': (str,),  # noqa: E501
            'gas_price': (str,),  # noqa: E501
            'input_data': (str,),  # noqa: E501
            'max_fee_per_gas': (str,),  # noqa: E501
            'max_fee_priority_per_gas': (str,),  # noqa: E501
            'r': (str,),  # noqa: E501
            's': (str,),  # noqa: E501
            'v': (str,),  # noqa: E501
            'value': (str,),  # noqa: E501
            'locktime': (int,),  # noqa: E501
            'transaction_hash': (str,),  # noqa: E501
            'v_size': (int,),  # noqa: E501
            'version': (int,),  # noqa: E501
            'vin': ([DecodeRawTransactionHexRISZVinInner],),  # noqa: E501
            'vout': ([DecodeRawTransactionHexRISZVoutInner],),  # noqa: E501
            'gas_limit': (str,),  # noqa: E501
            'nonce': (int,),  # noqa: E501
            'recipient': (str,),  # noqa: E501
            'sender': (str,),  # noqa: E501
            'type': (int,),  # noqa: E501
            'expiry_height': (int,),  # noqa: E501
            'overwintered': (bool,),  # noqa: E501
            'saplinged': (bool,),  # noqa: E501
            'value_balance': (str,),  # noqa: E501
            'version_group_id': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'weight': 'weight',  # noqa: E501
        'approximate_fee': 'approximateFee',  # noqa: E501
        'approximate_minimum_required_fee': 'approximateMinimumRequiredFee',  # noqa: E501
        'gas_paid_for_data': 'gasPaidForData',  # noqa: E501
        'gas_price': 'gasPrice',  # noqa: E501
        'input_data': 'inputData',  # noqa: E501
        'max_fee_per_gas': 'maxFeePerGas',  # noqa: E501
        'max_fee_priority_per_gas': 'maxFeePriorityPerGas',  # noqa: E501
        'r': 'r',  # noqa: E501
        's': 's',  # noqa: E501
        'v': 'v',  # noqa: E501
        'value': 'value',  # noqa: E501
        'locktime': 'locktime',  # noqa: E501
        'transaction_hash': 'transactionHash',  # noqa: E501
        'v_size': 'vSize',  # noqa: E501
        'version': 'version',  # noqa: E501
        'vin': 'vin',  # noqa: E501
        'vout': 'vout',  # noqa: E501
        'gas_limit': 'gasLimit',  # noqa: E501
        'nonce': 'nonce',  # noqa: E501
        'recipient': 'recipient',  # noqa: E501
        'sender': 'sender',  # noqa: E501
        'type': 'type',  # noqa: E501
        'expiry_height': 'expiryHeight',  # noqa: E501
        'overwintered': 'overwintered',  # noqa: E501
        'saplinged': 'saplinged',  # noqa: E501
        'value_balance': 'valueBalance',  # noqa: E501
        'version_group_id': 'versionGroupId',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """DecodeRawTransactionHexRIS - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            weight (int): Represents the size of a block, measured in weight units and including the segwit discount.. [optional]  # noqa: E501
            approximate_fee (str): Defines the approximate fee value. When isConfirmed is True - Defines the amount of the transaction fee When isConfirmed is False - For ETH-based blockchains this attribute represents the max fee value.. [optional]  # noqa: E501
            approximate_minimum_required_fee (str): Defines the approximate minimum fee that is required for the transaction.. [optional]  # noqa: E501
            gas_paid_for_data (str): Represents the amount of gas paid for the data in the transaction.. [optional]  # noqa: E501
            gas_price (str): Represents the price offered to the miner to purchase this amount of gas.. [optional]  # noqa: E501
            input_data (str): Represents additional information that is required for the transaction.. [optional]  # noqa: E501
            max_fee_per_gas (str): Defines the maximum amount that customer is willing to pay per unit of gas to get his transaction included in a block.. [optional]  # noqa: E501
            max_fee_priority_per_gas (str): Represents determined by the user value that is paid directly to miners.. [optional]  # noqa: E501
            r (str): Represents output of an ECDSA signature.. [optional]  # noqa: E501
            s (str): Represents output of an ECDSA signature.. [optional]  # noqa: E501
            v (str): Defines the the recovery id.. [optional]  # noqa: E501
            value (str): Represents the sent/received amount.. [optional]  # noqa: E501
            locktime (int): Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid.. [optional]  # noqa: E501
            transaction_hash (str): Represents the same as transactionId for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols hash is different from transactionId for SegWit transactions.. [optional]  # noqa: E501
            v_size (int): Represents the virtual size of this transaction.. [optional]  # noqa: E501
            version (int): Represents the transaction version number.. [optional]  # noqa: E501
            vin ([DecodeRawTransactionHexRISZVinInner]): Represents the Inputs of the transaction. [optional]  # noqa: E501
            vout ([DecodeRawTransactionHexRISZVoutInner]): Represents the Inputs of the transaction. [optional]  # noqa: E501
            gas_limit (str): Represents the amount of gas used by this specific transaction alone.. [optional]  # noqa: E501
            nonce (int): Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender's address.. [optional]  # noqa: E501
            recipient (str): The address which receives this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one recipient.. [optional]  # noqa: E501
            sender (str): Represents the address which sends this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one sender.. [optional]  # noqa: E501
            type (int): Specifies the transaction type as one from three options: if response returns a `\"0\"` it means the raw transaction includes legacy transaction data, if it is `\"1\"` - includes access lists for EIP2930, and if it is `\"2\"` - EIP1559 data.. [optional]  # noqa: E501
            expiry_height (int): Represents a block height after which the transaction will expire.. [optional]  # noqa: E501
            overwintered (bool): \"Overwinter\" is the network upgrade for the Zcash blockchain.. [optional]  # noqa: E501
            saplinged (bool): Defines if the transaction includes sapling or not.. [optional]  # noqa: E501
            value_balance (str): Defines the transaction value balance.. [optional]  # noqa: E501
            version_group_id (str): Represents the transaction version group ID. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """DecodeRawTransactionHexRIS - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            weight (int): Represents the size of a block, measured in weight units and including the segwit discount.. [optional]  # noqa: E501
            approximate_fee (str): Defines the approximate fee value. When isConfirmed is True - Defines the amount of the transaction fee When isConfirmed is False - For ETH-based blockchains this attribute represents the max fee value.. [optional]  # noqa: E501
            approximate_minimum_required_fee (str): Defines the approximate minimum fee that is required for the transaction.. [optional]  # noqa: E501
            gas_paid_for_data (str): Represents the amount of gas paid for the data in the transaction.. [optional]  # noqa: E501
            gas_price (str): Represents the price offered to the miner to purchase this amount of gas.. [optional]  # noqa: E501
            input_data (str): Represents additional information that is required for the transaction.. [optional]  # noqa: E501
            max_fee_per_gas (str): Defines the maximum amount that customer is willing to pay per unit of gas to get his transaction included in a block.. [optional]  # noqa: E501
            max_fee_priority_per_gas (str): Represents determined by the user value that is paid directly to miners.. [optional]  # noqa: E501
            r (str): Represents output of an ECDSA signature.. [optional]  # noqa: E501
            s (str): Represents output of an ECDSA signature.. [optional]  # noqa: E501
            v (str): Defines the the recovery id.. [optional]  # noqa: E501
            value (str): Represents the sent/received amount.. [optional]  # noqa: E501
            locktime (int): Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid.. [optional]  # noqa: E501
            transaction_hash (str): Represents the same as transactionId for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols hash is different from transactionId for SegWit transactions.. [optional]  # noqa: E501
            v_size (int): Represents the virtual size of this transaction.. [optional]  # noqa: E501
            version (int): Represents the transaction version number.. [optional]  # noqa: E501
            vin ([DecodeRawTransactionHexRISZVinInner]): Represents the Inputs of the transaction. [optional]  # noqa: E501
            vout ([DecodeRawTransactionHexRISZVoutInner]): Represents the Inputs of the transaction. [optional]  # noqa: E501
            gas_limit (str): Represents the amount of gas used by this specific transaction alone.. [optional]  # noqa: E501
            nonce (int): Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender's address.. [optional]  # noqa: E501
            recipient (str): The address which receives this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one recipient.. [optional]  # noqa: E501
            sender (str): Represents the address which sends this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one sender.. [optional]  # noqa: E501
            type (int): Specifies the transaction type as one from three options: if response returns a `\"0\"` it means the raw transaction includes legacy transaction data, if it is `\"1\"` - includes access lists for EIP2930, and if it is `\"2\"` - EIP1559 data.. [optional]  # noqa: E501
            expiry_height (int): Represents a block height after which the transaction will expire.. [optional]  # noqa: E501
            overwintered (bool): \"Overwinter\" is the network upgrade for the Zcash blockchain.. [optional]  # noqa: E501
            saplinged (bool): Defines if the transaction includes sapling or not.. [optional]  # noqa: E501
            value_balance (str): Defines the transaction value balance.. [optional]  # noqa: E501
            version_group_id (str): Represents the transaction version group ID. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
          ],
          'oneOf': [
              DecodeRawTransactionHexRISB,
              DecodeRawTransactionHexRISB2,
              DecodeRawTransactionHexRISB22,
              DecodeRawTransactionHexRISD,
              DecodeRawTransactionHexRISD2,
              DecodeRawTransactionHexRISE,
              DecodeRawTransactionHexRISE2,
              DecodeRawTransactionHexRISL,
              DecodeRawTransactionHexRISZ,
          ],
        }
