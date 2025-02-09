# cryptoapis.InformativeApi

All URIs are relative to *https://rest.cryptoapis.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction_request_details**](InformativeApi.md#get_transaction_request_details) | **GET** /wallet-as-a-service/transactionRequests/{transactionRequestId} | Get Transaction Request Details
[**get_wallet_asset_details**](InformativeApi.md#get_wallet_asset_details) | **GET** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network} | Get Wallet Asset Details
[**get_wallet_transaction_details_by_transaction_id**](InformativeApi.md#get_wallet_transaction_details_by_transaction_id) | **GET** /wallet-as-a-service/wallets/{blockchain}/{network}/transactions/{transactionId} | Get Wallet Transaction Details By Transaction ID
[**list_all_assets_by_wallet_id**](InformativeApi.md#list_all_assets_by_wallet_id) | **GET** /wallet-as-a-service/wallets/{walletId}/assets | List All Assets By Wallet ID
[**list_all_assets_from_all_wallets**](InformativeApi.md#list_all_assets_from_all_wallets) | **GET** /wallet-as-a-service/wallets/all-assets | List All Assets From All Wallets
[**list_deposit_addresses**](InformativeApi.md#list_deposit_addresses) | **GET** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network}/addresses | List Deposit Addresses
[**list_supported_tokens**](InformativeApi.md#list_supported_tokens) | **GET** /wallet-as-a-service/info/{blockchain}/{network}/supported-tokens | List Supported Tokens
[**list_wallet_transactions**](InformativeApi.md#list_wallet_transactions) | **GET** /wallet-as-a-service/wallets/{walletId}/{blockchain}/{network}/transactions | List Wallet Transactions


# **get_transaction_request_details**
> GetTransactionRequestDetailsR get_transaction_request_details(transaction_request_id)

Get Transaction Request Details

Through this endpoint customers can obtain details on transaction request.    {note}This regards **transaction requests**, which is not to be confused with **transactions**. Transaction requests may not be approved due to any reason, hence a transaction may not occur.{/note}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import informative_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.get_transaction_request_details403_response import GetTransactionRequestDetails403Response
from cryptoapis.model.get_transaction_request_details400_response import GetTransactionRequestDetails400Response
from cryptoapis.model.get_transaction_request_details_r import GetTransactionRequestDetailsR
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.convert_bitcoin_cash_address409_response import ConvertBitcoinCashAddress409Response
from cryptoapis.model.get_transaction_request_details401_response import GetTransactionRequestDetails401Response
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = informative_api.InformativeApi(api_client)
    transaction_request_id = "6115126693397c0006f78eb4" # str | Represents the unique ID of the transaction request.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Transaction Request Details
        api_response = api_instance.get_transaction_request_details(transaction_request_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->get_transaction_request_details: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Transaction Request Details
        api_response = api_instance.get_transaction_request_details(transaction_request_id, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->get_transaction_request_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_request_id** | **str**| Represents the unique ID of the transaction request. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetTransactionRequestDetailsR**](GetTransactionRequestDetailsR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet_asset_details**
> GetWalletAssetDetailsR get_wallet_asset_details(blockchain, network, wallet_id)

Get Wallet Asset Details

Through this endpoint customers can obtain details on all assets (coins, fungible tokens, non-fungible tokens) for the entire Wallet.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import informative_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.get_wallet_asset_details401_response import GetWalletAssetDetails401Response
from cryptoapis.model.get_wallet_asset_details403_response import GetWalletAssetDetails403Response
from cryptoapis.model.get_xrp_ripple_transaction_details_by_transaction_id404_response import GetXRPRippleTransactionDetailsByTransactionID404Response
from cryptoapis.model.get_wallet_asset_details_r import GetWalletAssetDetailsR
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.get_wallet_asset_details400_response import GetWalletAssetDetails400Response
from cryptoapis.model.convert_bitcoin_cash_address409_response import ConvertBitcoinCashAddress409Response
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = informative_api.InformativeApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    wallet_id = "60c9d9921c38030006675ff6" # str | Defines the unique ID of the Wallet.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Wallet Asset Details
        api_response = api_instance.get_wallet_asset_details(blockchain, network, wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->get_wallet_asset_details: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Wallet Asset Details
        api_response = api_instance.get_wallet_asset_details(blockchain, network, wallet_id, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->get_wallet_asset_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **wallet_id** | **str**| Defines the unique ID of the Wallet. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetWalletAssetDetailsR**](GetWalletAssetDetailsR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**404** | The specified resource has not been found. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet_transaction_details_by_transaction_id**
> GetWalletTransactionDetailsByTransactionIDR get_wallet_transaction_details_by_transaction_id(blockchain, network, transaction_id)

Get Wallet Transaction Details By Transaction ID

Through this endpoint users can obtain Wallet transaction information by providing a `transactionId`. Customers can receive information only for a transaction that has been made from their own wallet.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import informative_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.get_wallet_transaction_details_by_transaction_id401_response import GetWalletTransactionDetailsByTransactionID401Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.get_wallet_transaction_details_by_transaction_id400_response import GetWalletTransactionDetailsByTransactionID400Response
from cryptoapis.model.get_xrp_ripple_transaction_details_by_transaction_id404_response import GetXRPRippleTransactionDetailsByTransactionID404Response
from cryptoapis.model.get_wallet_transaction_details_by_transaction_idr import GetWalletTransactionDetailsByTransactionIDR
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.convert_bitcoin_cash_address409_response import ConvertBitcoinCashAddress409Response
from cryptoapis.model.get_wallet_transaction_details_by_transaction_id403_response import GetWalletTransactionDetailsByTransactionID403Response
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = informative_api.InformativeApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    transaction_id = "3e081861494aed897e589cdeab5d9e628d985e571ed1c19896d1aa698cce9d80" # str | Represents the unique identifier of a transaction, i.e. it could be `transactionId` in UTXO-based protocols like Bitcoin, and transaction `hash` in Ethereum blockchain.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Wallet Transaction Details By Transaction ID
        api_response = api_instance.get_wallet_transaction_details_by_transaction_id(blockchain, network, transaction_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->get_wallet_transaction_details_by_transaction_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Wallet Transaction Details By Transaction ID
        api_response = api_instance.get_wallet_transaction_details_by_transaction_id(blockchain, network, transaction_id, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->get_wallet_transaction_details_by_transaction_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **transaction_id** | **str**| Represents the unique identifier of a transaction, i.e. it could be &#x60;transactionId&#x60; in UTXO-based protocols like Bitcoin, and transaction &#x60;hash&#x60; in Ethereum blockchain. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetWalletTransactionDetailsByTransactionIDR**](GetWalletTransactionDetailsByTransactionIDR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**404** | The specified resource has not been found. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_assets_by_wallet_id**
> ListAllAssetsByWalletIDR list_all_assets_by_wallet_id(wallet_id)

List All Assets By Wallet ID

Through this endpoint customers can obtain information about available assets in one of their wallets, regardless of the blockchain protocol or network, by providing walletId.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import informative_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.list_all_assets_by_wallet_idr import ListAllAssetsByWalletIDR
from cryptoapis.model.list_all_assets_by_wallet_id403_response import ListAllAssetsByWalletID403Response
from cryptoapis.model.list_all_assets_by_wallet_id400_response import ListAllAssetsByWalletID400Response
from cryptoapis.model.get_xrp_ripple_transaction_details_by_transaction_id404_response import GetXRPRippleTransactionDetailsByTransactionID404Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.list_all_assets_by_wallet_id401_response import ListAllAssetsByWalletID401Response
from cryptoapis.model.convert_bitcoin_cash_address409_response import ConvertBitcoinCashAddress409Response
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = informative_api.InformativeApi(api_client)
    wallet_id = "60c9d9921c38030006675ff6" # str | Defines the unique ID of the Wallet.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List All Assets By Wallet ID
        api_response = api_instance.list_all_assets_by_wallet_id(wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->list_all_assets_by_wallet_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Assets By Wallet ID
        api_response = api_instance.list_all_assets_by_wallet_id(wallet_id, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->list_all_assets_by_wallet_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Defines the unique ID of the Wallet. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**ListAllAssetsByWalletIDR**](ListAllAssetsByWalletIDR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**404** | The specified resource has not been found. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_assets_from_all_wallets**
> ListAllAssetsFromAllWalletsR list_all_assets_from_all_wallets()

List All Assets From All Wallets

Through this endpoint customers can obtain information about available assets in all of their wallets, regardless of the blockchain protocol or network.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import informative_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.list_all_assets_from_all_wallets401_response import ListAllAssetsFromAllWallets401Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.list_all_assets_from_all_wallets_r import ListAllAssetsFromAllWalletsR
from cryptoapis.model.list_all_assets_from_all_wallets400_response import ListAllAssetsFromAllWallets400Response
from cryptoapis.model.list_all_assets_from_all_wallets403_response import ListAllAssetsFromAllWallets403Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.convert_bitcoin_cash_address409_response import ConvertBitcoinCashAddress409Response
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = informative_api.InformativeApi(api_client)
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Assets From All Wallets
        api_response = api_instance.list_all_assets_from_all_wallets(context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->list_all_assets_from_all_wallets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListAllAssetsFromAllWalletsR**](ListAllAssetsFromAllWalletsR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deposit_addresses**
> ListDepositAddressesR list_deposit_addresses(blockchain, network, wallet_id)

List Deposit Addresses

Through this endpoint customers can pull a list of Deposit/Receiving Addresses they have already generated.    {note}Please note that listing data from the same type will apply pagination on the results.{/note}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import informative_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.list_deposit_addresses_r import ListDepositAddressesR
from cryptoapis.model.list_deposit_addresses401_response import ListDepositAddresses401Response
from cryptoapis.model.list_deposit_addresses403_response import ListDepositAddresses403Response
from cryptoapis.model.list_deposit_addresses400_response import ListDepositAddresses400Response
from cryptoapis.model.get_xrp_ripple_transaction_details_by_transaction_id404_response import GetXRPRippleTransactionDetailsByTransactionID404Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.convert_bitcoin_cash_address409_response import ConvertBitcoinCashAddress409Response
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = informative_api.InformativeApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    wallet_id = "60c9d9921c38030006675ff6" # str | Represents the unique ID of the specific Wallet.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Deposit Addresses
        api_response = api_instance.list_deposit_addresses(blockchain, network, wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->list_deposit_addresses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Deposit Addresses
        api_response = api_instance.list_deposit_addresses(blockchain, network, wallet_id, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->list_deposit_addresses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **wallet_id** | **str**| Represents the unique ID of the specific Wallet. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**ListDepositAddressesR**](ListDepositAddressesR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**404** | The specified resource has not been found. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supported_tokens**
> ListSupportedTokensR list_supported_tokens(blockchain, network)

List Supported Tokens

Through this endpoint customers can obtain information on multiple tokens at once.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import informative_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.list_supported_tokens403_response import ListSupportedTokens403Response
from cryptoapis.model.list_supported_tokens_r import ListSupportedTokensR
from cryptoapis.model.list_supported_tokens400_response import ListSupportedTokens400Response
from cryptoapis.model.list_supported_tokens401_response import ListSupportedTokens401Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.convert_bitcoin_cash_address409_response import ConvertBitcoinCashAddress409Response
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = informative_api.InformativeApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Supported Tokens
        api_response = api_instance.list_supported_tokens(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->list_supported_tokens: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Supported Tokens
        api_response = api_instance.list_supported_tokens(blockchain, network, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->list_supported_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListSupportedTokensR**](ListSupportedTokensR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_wallet_transactions**
> ListWalletTransactionsR list_wallet_transactions(blockchain, network, wallet_id)

List Wallet Transactions

Through this endpoint customers can list Transactions from and to their Wallet. The data returned will include `transactionId`, `direction` of the transaction - incoming or outgoing, `amount` and more.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import informative_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.list_wallet_transactions_r import ListWalletTransactionsR
from cryptoapis.model.list_wallet_transactions400_response import ListWalletTransactions400Response
from cryptoapis.model.list_wallet_transactions403_response import ListWalletTransactions403Response
from cryptoapis.model.list_wallet_transactions401_response import ListWalletTransactions401Response
from cryptoapis.model.get_xrp_ripple_transaction_details_by_transaction_id404_response import GetXRPRippleTransactionDetailsByTransactionID404Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.convert_bitcoin_cash_address409_response import ConvertBitcoinCashAddress409Response
from cryptoapis.model.convert_bitcoin_cash_address415_response import ConvertBitcoinCashAddress415Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.cryptoapis.io
# See configuration.py for a list of all supported configuration parameters.
configuration = cryptoapis.Configuration(
    host = "https://rest.cryptoapis.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with cryptoapis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = informative_api.InformativeApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    wallet_id = "60c9d9921c38030006675ff6" # str | Represents the unique ID of the specific Wallet.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Wallet Transactions
        api_response = api_instance.list_wallet_transactions(blockchain, network, wallet_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->list_wallet_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Wallet Transactions
        api_response = api_instance.list_wallet_transactions(blockchain, network, wallet_id, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling InformativeApi->list_wallet_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **wallet_id** | **str**| Represents the unique ID of the specific Wallet. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListWalletTransactionsR**](ListWalletTransactionsR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has been successful. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**404** | The specified resource has not been found. |  -  |
**409** | The data provided seems to be invalid. |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

