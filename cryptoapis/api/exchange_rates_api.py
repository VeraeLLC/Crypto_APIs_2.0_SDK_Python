"""
    CryptoAPIs

    Crypto APIs is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2021-03-20
    Contact: developers@cryptoapis.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cryptoapis.api_client import ApiClient, Endpoint as _Endpoint
from cryptoapis.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.convert_bitcoin_cash_address409_response import ConvertBitcoinCashAddress409Response
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.get_exchange_rate_by_asset_symbols400_response import GetExchangeRateByAssetSymbols400Response
from cryptoapis.model.get_exchange_rate_by_asset_symbols401_response import GetExchangeRateByAssetSymbols401Response
from cryptoapis.model.get_exchange_rate_by_asset_symbols403_response import GetExchangeRateByAssetSymbols403Response
from cryptoapis.model.get_exchange_rate_by_asset_symbols422_response import GetExchangeRateByAssetSymbols422Response
from cryptoapis.model.get_exchange_rate_by_asset_symbols_r import GetExchangeRateByAssetSymbolsR
from cryptoapis.model.get_exchange_rate_by_assets_ids400_response import GetExchangeRateByAssetsIDs400Response
from cryptoapis.model.get_exchange_rate_by_assets_ids401_response import GetExchangeRateByAssetsIDs401Response
from cryptoapis.model.get_exchange_rate_by_assets_ids403_response import GetExchangeRateByAssetsIDs403Response
from cryptoapis.model.get_exchange_rate_by_assets_ids422_response import GetExchangeRateByAssetsIDs422Response
from cryptoapis.model.get_exchange_rate_by_assets_ids_r import GetExchangeRateByAssetsIDsR


class ExchangeRatesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_exchange_rate_by_asset_symbols_endpoint = _Endpoint(
            settings={
                'response_type': (GetExchangeRateByAssetSymbolsR,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/market-data/exchange-rates/by-symbols/{fromAssetSymbol}/{toAssetSymbol}',
                'operation_id': 'get_exchange_rate_by_asset_symbols',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'from_asset_symbol',
                    'to_asset_symbol',
                    'context',
                    'calculation_timestamp',
                ],
                'required': [
                    'from_asset_symbol',
                    'to_asset_symbol',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'from_asset_symbol':
                        (str,),
                    'to_asset_symbol':
                        (str,),
                    'context':
                        (str,),
                    'calculation_timestamp':
                        (int,),
                },
                'attribute_map': {
                    'from_asset_symbol': 'fromAssetSymbol',
                    'to_asset_symbol': 'toAssetSymbol',
                    'context': 'context',
                    'calculation_timestamp': 'calculationTimestamp',
                },
                'location_map': {
                    'from_asset_symbol': 'path',
                    'to_asset_symbol': 'path',
                    'context': 'query',
                    'calculation_timestamp': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_exchange_rate_by_assets_ids_endpoint = _Endpoint(
            settings={
                'response_type': (GetExchangeRateByAssetsIDsR,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/market-data/exchange-rates/by-asset-ids/{fromAssetId}/{toAssetId}',
                'operation_id': 'get_exchange_rate_by_assets_ids',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'from_asset_id',
                    'to_asset_id',
                    'context',
                    'calculation_timestamp',
                ],
                'required': [
                    'from_asset_id',
                    'to_asset_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'from_asset_id':
                        (str,),
                    'to_asset_id':
                        (str,),
                    'context':
                        (str,),
                    'calculation_timestamp':
                        (int,),
                },
                'attribute_map': {
                    'from_asset_id': 'fromAssetId',
                    'to_asset_id': 'toAssetId',
                    'context': 'context',
                    'calculation_timestamp': 'calculationTimestamp',
                },
                'location_map': {
                    'from_asset_id': 'path',
                    'to_asset_id': 'path',
                    'context': 'query',
                    'calculation_timestamp': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_exchange_rate_by_asset_symbols(
        self,
        from_asset_symbol,
        to_asset_symbol,
        **kwargs
    ):
        """Get Exchange Rate By Asset Symbols  # noqa: E501

        Through this endpoint customers can obtain exchange rates by asset symbols. The process represents the exchange rate value of a single unit of one asset versus another one. Data is provided per unique asset symbol.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_exchange_rate_by_asset_symbols(from_asset_symbol, to_asset_symbol, async_req=True)
        >>> result = thread.get()

        Args:
            from_asset_symbol (str): Defines the base asset symbol to get a rate for.
            to_asset_symbol (str): Defines the relation asset symbol in which the base asset rate will be displayed.

        Keyword Args:
            context (str): In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.. [optional]
            calculation_timestamp (int): Defines the time of the market data used to calculate the exchange rate in UNIX Timestamp. Oldest possible timestamp is 30 days.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            GetExchangeRateByAssetSymbolsR
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['from_asset_symbol'] = \
            from_asset_symbol
        kwargs['to_asset_symbol'] = \
            to_asset_symbol
        return self.get_exchange_rate_by_asset_symbols_endpoint.call_with_http_info(**kwargs)

    def get_exchange_rate_by_assets_ids(
        self,
        from_asset_id,
        to_asset_id,
        **kwargs
    ):
        """Get Exchange Rate By Assets IDs  # noqa: E501

        Through this endpoint customers can obtain exchange rates by asset IDs. The process represents the exchange rate value of a single unit of one asset versus another one. Data is provided per unique asset Reference ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_exchange_rate_by_assets_ids(from_asset_id, to_asset_id, async_req=True)
        >>> result = thread.get()

        Args:
            from_asset_id (str): Defines the base asset Reference ID to get a rate for.
            to_asset_id (str): Defines the relation asset Reference ID in which the base asset rate will be displayed.

        Keyword Args:
            context (str): In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.. [optional]
            calculation_timestamp (int): Defines the time of the market data used to calculate the exchange rate in UNIX Timestamp. Oldest possible timestamp is 30 days.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            GetExchangeRateByAssetsIDsR
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['from_asset_id'] = \
            from_asset_id
        kwargs['to_asset_id'] = \
            to_asset_id
        return self.get_exchange_rate_by_assets_ids_endpoint.call_with_http_info(**kwargs)

