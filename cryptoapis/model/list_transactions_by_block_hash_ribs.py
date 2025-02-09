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
    from cryptoapis.model.get_transaction_details_by_transaction_idribsz_vout_inner import GetTransactionDetailsByTransactionIDRIBSZVoutInner
    from cryptoapis.model.get_transaction_details_by_transaction_idribszv_shielded_output_inner import GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner
    from cryptoapis.model.get_transaction_details_by_transaction_idribszv_shielded_spend_inner import GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner
    from cryptoapis.model.list_transactions_by_block_hash_ribsb import ListTransactionsByBlockHashRIBSB
    from cryptoapis.model.list_transactions_by_block_hash_ribsbc import ListTransactionsByBlockHashRIBSBC
    from cryptoapis.model.list_transactions_by_block_hash_ribsbsc import ListTransactionsByBlockHashRIBSBSC
    from cryptoapis.model.list_transactions_by_block_hash_ribsbsc_gas_price import ListTransactionsByBlockHashRIBSBSCGasPrice
    from cryptoapis.model.list_transactions_by_block_hash_ribsd import ListTransactionsByBlockHashRIBSD
    from cryptoapis.model.list_transactions_by_block_hash_ribsd2 import ListTransactionsByBlockHashRIBSD2
    from cryptoapis.model.list_transactions_by_block_hash_ribse import ListTransactionsByBlockHashRIBSE
    from cryptoapis.model.list_transactions_by_block_hash_ribsec import ListTransactionsByBlockHashRIBSEC
    from cryptoapis.model.list_transactions_by_block_hash_ribsl import ListTransactionsByBlockHashRIBSL
    from cryptoapis.model.list_transactions_by_block_hash_ribsz import ListTransactionsByBlockHashRIBSZ
    from cryptoapis.model.list_transactions_by_block_hash_ribsz_vin_inner import ListTransactionsByBlockHashRIBSZVinInner
    from cryptoapis.model.list_transactions_by_block_hash_ribszv_join_split_inner import ListTransactionsByBlockHashRIBSZVJoinSplitInner
    globals()['GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner'] = GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner
    globals()['GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner'] = GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner
    globals()['GetTransactionDetailsByTransactionIDRIBSZVoutInner'] = GetTransactionDetailsByTransactionIDRIBSZVoutInner
    globals()['ListTransactionsByBlockHashRIBSB'] = ListTransactionsByBlockHashRIBSB
    globals()['ListTransactionsByBlockHashRIBSBC'] = ListTransactionsByBlockHashRIBSBC
    globals()['ListTransactionsByBlockHashRIBSBSC'] = ListTransactionsByBlockHashRIBSBSC
    globals()['ListTransactionsByBlockHashRIBSBSCGasPrice'] = ListTransactionsByBlockHashRIBSBSCGasPrice
    globals()['ListTransactionsByBlockHashRIBSD'] = ListTransactionsByBlockHashRIBSD
    globals()['ListTransactionsByBlockHashRIBSD2'] = ListTransactionsByBlockHashRIBSD2
    globals()['ListTransactionsByBlockHashRIBSE'] = ListTransactionsByBlockHashRIBSE
    globals()['ListTransactionsByBlockHashRIBSEC'] = ListTransactionsByBlockHashRIBSEC
    globals()['ListTransactionsByBlockHashRIBSL'] = ListTransactionsByBlockHashRIBSL
    globals()['ListTransactionsByBlockHashRIBSZ'] = ListTransactionsByBlockHashRIBSZ
    globals()['ListTransactionsByBlockHashRIBSZVJoinSplitInner'] = ListTransactionsByBlockHashRIBSZVJoinSplitInner
    globals()['ListTransactionsByBlockHashRIBSZVinInner'] = ListTransactionsByBlockHashRIBSZVinInner


class ListTransactionsByBlockHashRIBS(ModelComposed):
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
            'locktime': (int,),  # noqa: E501
            'size': (int,),  # noqa: E501
            'v_size': (int,),  # noqa: E501
            'version': (int,),  # noqa: E501
            'vin': ([ListTransactionsByBlockHashRIBSZVinInner],),  # noqa: E501
            'vout': ([GetTransactionDetailsByTransactionIDRIBSZVoutInner],),  # noqa: E501
            'contract': (str,),  # noqa: E501
            'gas_limit': (str,),  # noqa: E501
            'gas_price': (ListTransactionsByBlockHashRIBSBSCGasPrice,),  # noqa: E501
            'gas_used': (str,),  # noqa: E501
            'input_data': (str,),  # noqa: E501
            'nonce': (int,),  # noqa: E501
            'transaction_status': (str,),  # noqa: E501
            'binding_sig': (str,),  # noqa: E501
            'expiry_height': (int,),  # noqa: E501
            'join_split_pub_key': (str,),  # noqa: E501
            'join_split_sig': (str,),  # noqa: E501
            'overwintered': (bool,),  # noqa: E501
            'v_join_split': ([ListTransactionsByBlockHashRIBSZVJoinSplitInner],),  # noqa: E501
            'v_shielded_output': ([GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner],),  # noqa: E501
            'v_shielded_spend': ([GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner],),  # noqa: E501
            'value_balance': (str,),  # noqa: E501
            'version_group_id': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'locktime': 'locktime',  # noqa: E501
        'size': 'size',  # noqa: E501
        'v_size': 'vSize',  # noqa: E501
        'version': 'version',  # noqa: E501
        'vin': 'vin',  # noqa: E501
        'vout': 'vout',  # noqa: E501
        'contract': 'contract',  # noqa: E501
        'gas_limit': 'gasLimit',  # noqa: E501
        'gas_price': 'gasPrice',  # noqa: E501
        'gas_used': 'gasUsed',  # noqa: E501
        'input_data': 'inputData',  # noqa: E501
        'nonce': 'nonce',  # noqa: E501
        'transaction_status': 'transactionStatus',  # noqa: E501
        'binding_sig': 'bindingSig',  # noqa: E501
        'expiry_height': 'expiryHeight',  # noqa: E501
        'join_split_pub_key': 'joinSplitPubKey',  # noqa: E501
        'join_split_sig': 'joinSplitSig',  # noqa: E501
        'overwintered': 'overwintered',  # noqa: E501
        'v_join_split': 'vJoinSplit',  # noqa: E501
        'v_shielded_output': 'vShieldedOutput',  # noqa: E501
        'v_shielded_spend': 'vShieldedSpend',  # noqa: E501
        'value_balance': 'valueBalance',  # noqa: E501
        'version_group_id': 'versionGroupId',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ListTransactionsByBlockHashRIBS - a model defined in OpenAPI

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
            locktime (int): Represents the time at which a particular transaction can be added to the blockchain.. [optional]  # noqa: E501
            size (int): Represents the total size of this transaction.. [optional]  # noqa: E501
            v_size (int): Represents the virtual size of this transaction.. [optional]  # noqa: E501
            version (int): Numeric representation of the transaction Represents the transaction version number.. [optional]  # noqa: E501
            vin ([ListTransactionsByBlockHashRIBSZVinInner]): Object Array representation of transaction inputs. [optional]  # noqa: E501
            vout ([GetTransactionDetailsByTransactionIDRIBSZVoutInner]): Object Array representation of transaction outputs. [optional]  # noqa: E501
            contract (str): Represents the specific transaction contract.. [optional]  # noqa: E501
            gas_limit (str): Represents the amount of gas used by this specific transaction alone.. [optional]  # noqa: E501
            gas_price (ListTransactionsByBlockHashRIBSBSCGasPrice): [optional]  # noqa: E501
            gas_used (str): Represents the exact unit of gas that was used for the transaction.. [optional]  # noqa: E501
            input_data (str): Represents additional information that is required for the transaction.. [optional]  # noqa: E501
            nonce (int): Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender's address.. [optional]  # noqa: E501
            transaction_status (str): Represents the status of this transaction. [optional]  # noqa: E501
            binding_sig (str): It is used to enforce balance of Spend and Output transfers, in order to prevent their replay across transactions.. [optional]  # noqa: E501
            expiry_height (int): Represents a block height after which the transaction will expire.. [optional]  # noqa: E501
            join_split_pub_key (str): Represents an encoding of a JoinSplitSig public validating key.. [optional]  # noqa: E501
            join_split_sig (str): Is used to sign transactions that contain at least one JoinSplit description.. [optional]  # noqa: E501
            overwintered (bool): \"Overwinter\" is the network upgrade for the Zcash blockchain.. [optional]  # noqa: E501
            v_join_split ([ListTransactionsByBlockHashRIBSZVJoinSplitInner]): Represents a sequence of JoinSplit descriptions using BCTV14 proofs.. [optional]  # noqa: E501
            v_shielded_output ([GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner]): Object Array representation of transaction output descriptions. [optional]  # noqa: E501
            v_shielded_spend ([GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner]): Object Array representation of transaction spend descriptions. [optional]  # noqa: E501
            value_balance (str): Defines the transaction value balance.. [optional]  # noqa: E501
            version_group_id (str): Represents the transaction version group ID.. [optional]  # noqa: E501
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
        """ListTransactionsByBlockHashRIBS - a model defined in OpenAPI

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
            locktime (int): Represents the time at which a particular transaction can be added to the blockchain.. [optional]  # noqa: E501
            size (int): Represents the total size of this transaction.. [optional]  # noqa: E501
            v_size (int): Represents the virtual size of this transaction.. [optional]  # noqa: E501
            version (int): Numeric representation of the transaction Represents the transaction version number.. [optional]  # noqa: E501
            vin ([ListTransactionsByBlockHashRIBSZVinInner]): Object Array representation of transaction inputs. [optional]  # noqa: E501
            vout ([GetTransactionDetailsByTransactionIDRIBSZVoutInner]): Object Array representation of transaction outputs. [optional]  # noqa: E501
            contract (str): Represents the specific transaction contract.. [optional]  # noqa: E501
            gas_limit (str): Represents the amount of gas used by this specific transaction alone.. [optional]  # noqa: E501
            gas_price (ListTransactionsByBlockHashRIBSBSCGasPrice): [optional]  # noqa: E501
            gas_used (str): Represents the exact unit of gas that was used for the transaction.. [optional]  # noqa: E501
            input_data (str): Represents additional information that is required for the transaction.. [optional]  # noqa: E501
            nonce (int): Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender's address.. [optional]  # noqa: E501
            transaction_status (str): Represents the status of this transaction. [optional]  # noqa: E501
            binding_sig (str): It is used to enforce balance of Spend and Output transfers, in order to prevent their replay across transactions.. [optional]  # noqa: E501
            expiry_height (int): Represents a block height after which the transaction will expire.. [optional]  # noqa: E501
            join_split_pub_key (str): Represents an encoding of a JoinSplitSig public validating key.. [optional]  # noqa: E501
            join_split_sig (str): Is used to sign transactions that contain at least one JoinSplit description.. [optional]  # noqa: E501
            overwintered (bool): \"Overwinter\" is the network upgrade for the Zcash blockchain.. [optional]  # noqa: E501
            v_join_split ([ListTransactionsByBlockHashRIBSZVJoinSplitInner]): Represents a sequence of JoinSplit descriptions using BCTV14 proofs.. [optional]  # noqa: E501
            v_shielded_output ([GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner]): Object Array representation of transaction output descriptions. [optional]  # noqa: E501
            v_shielded_spend ([GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner]): Object Array representation of transaction spend descriptions. [optional]  # noqa: E501
            value_balance (str): Defines the transaction value balance.. [optional]  # noqa: E501
            version_group_id (str): Represents the transaction version group ID.. [optional]  # noqa: E501
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
              ListTransactionsByBlockHashRIBSB,
              ListTransactionsByBlockHashRIBSBC,
              ListTransactionsByBlockHashRIBSBSC,
              ListTransactionsByBlockHashRIBSD,
              ListTransactionsByBlockHashRIBSD2,
              ListTransactionsByBlockHashRIBSE,
              ListTransactionsByBlockHashRIBSEC,
              ListTransactionsByBlockHashRIBSL,
              ListTransactionsByBlockHashRIBSZ,
          ],
        }
