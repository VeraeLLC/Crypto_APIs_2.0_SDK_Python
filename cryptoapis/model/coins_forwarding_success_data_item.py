"""
    CryptoAPIs

    Crypto APIs 2.0 is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs 2.0 can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs 2.0 provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
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
)
from ..model_utils import OpenApiModel
from cryptoapis.exceptions import ApiAttributeError



class CoinsForwardingSuccessDataItem(ModelNormal):
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
        return {
            'blockchain': (str,),  # noqa: E501
            'network': (str,),  # noqa: E501
            'from_address': (str,),  # noqa: E501
            'to_address': (str,),  # noqa: E501
            'forwarded_amount': (str,),  # noqa: E501
            'forwarded_unit': (str,),  # noqa: E501
            'spent_fees_amount': (str,),  # noqa: E501
            'spent_fees_unit': (str,),  # noqa: E501
            'trigger_transaction_id': (str,),  # noqa: E501
            'forwarding_transaction_id': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'blockchain': 'blockchain',  # noqa: E501
        'network': 'network',  # noqa: E501
        'from_address': 'fromAddress',  # noqa: E501
        'to_address': 'toAddress',  # noqa: E501
        'forwarded_amount': 'forwardedAmount',  # noqa: E501
        'forwarded_unit': 'forwardedUnit',  # noqa: E501
        'spent_fees_amount': 'spentFeesAmount',  # noqa: E501
        'spent_fees_unit': 'spentFeesUnit',  # noqa: E501
        'trigger_transaction_id': 'triggerTransactionId',  # noqa: E501
        'forwarding_transaction_id': 'forwardingTransactionId',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, blockchain, network, from_address, to_address, forwarded_amount, forwarded_unit, spent_fees_amount, spent_fees_unit, trigger_transaction_id, forwarding_transaction_id, *args, **kwargs):  # noqa: E501
        """CoinsForwardingSuccessDataItem - a model defined in OpenAPI

        Args:
            blockchain (str): Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
            network (str): Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
            from_address (str): Represents the hash of the address that provides the coins.
            to_address (str): Represents the hash of the address to forward the coins to.
            forwarded_amount (str): Represents the amount of coins that have been forwarded.
            forwarded_unit (str): Represents the unit of coins that have been forwarded, e.g. BTC.
            spent_fees_amount (str): Represents the amount of the fee spent for the coins to be forwarded.
            spent_fees_unit (str): Represents the unit of the fee spent for the coins to be forwarded, e.g. BTC.
            trigger_transaction_id (str): Defines the unique Transaction ID that triggered the coin forwarding.
            forwarding_transaction_id (str): Defines the unique Transaction ID that forwarded the coins.

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
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
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

        self.blockchain = blockchain
        self.network = network
        self.from_address = from_address
        self.to_address = to_address
        self.forwarded_amount = forwarded_amount
        self.forwarded_unit = forwarded_unit
        self.spent_fees_amount = spent_fees_amount
        self.spent_fees_unit = spent_fees_unit
        self.trigger_transaction_id = trigger_transaction_id
        self.forwarding_transaction_id = forwarding_transaction_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
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
    ])

    @convert_js_args_to_python_args
    def __init__(self, blockchain, network, from_address, to_address, forwarded_amount, forwarded_unit, spent_fees_amount, spent_fees_unit, trigger_transaction_id, forwarding_transaction_id, *args, **kwargs):  # noqa: E501
        """CoinsForwardingSuccessDataItem - a model defined in OpenAPI

        Args:
            blockchain (str): Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
            network (str): Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
            from_address (str): Represents the hash of the address that provides the coins.
            to_address (str): Represents the hash of the address to forward the coins to.
            forwarded_amount (str): Represents the amount of coins that have been forwarded.
            forwarded_unit (str): Represents the unit of coins that have been forwarded, e.g. BTC.
            spent_fees_amount (str): Represents the amount of the fee spent for the coins to be forwarded.
            spent_fees_unit (str): Represents the unit of the fee spent for the coins to be forwarded, e.g. BTC.
            trigger_transaction_id (str): Defines the unique Transaction ID that triggered the coin forwarding.
            forwarding_transaction_id (str): Defines the unique Transaction ID that forwarded the coins.

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
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
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

        self.blockchain = blockchain
        self.network = network
        self.from_address = from_address
        self.to_address = to_address
        self.forwarded_amount = forwarded_amount
        self.forwarded_unit = forwarded_unit
        self.spent_fees_amount = spent_fees_amount
        self.spent_fees_unit = spent_fees_unit
        self.trigger_transaction_id = trigger_transaction_id
        self.forwarding_transaction_id = forwarding_transaction_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
