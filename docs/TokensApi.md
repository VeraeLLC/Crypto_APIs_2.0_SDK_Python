# cryptoapis.TokensApi

All URIs are relative to *https://rest.cryptoapis.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token_details_by_contract_address**](TokensApi.md#get_token_details_by_contract_address) | **GET** /blockchain-data/{blockchain}/{network}/addresses/{contractAddress}/contract | Get Token Details by Contract Address
[**list_confirmed_tokens_transfers_by_address**](TokensApi.md#list_confirmed_tokens_transfers_by_address) | **GET** /blockchain-data/{blockchain}/{network}/addresses/{address}/tokens-transfers | List Confirmed Tokens Transfers By Address
[**list_tokens_by_address**](TokensApi.md#list_tokens_by_address) | **GET** /blockchain-data/{blockchain}/{network}/addresses/{address}/tokens | List Tokens By Address
[**list_tokens_transfers_by_transaction_hash**](TokensApi.md#list_tokens_transfers_by_transaction_hash) | **GET** /blockchain-data/{blockchain}/{network}/transactions/{transactionHash}/tokens-transfers | List Tokens Transfers By Transaction Hash
[**list_unconfirmed_tokens_transfers_by_address**](TokensApi.md#list_unconfirmed_tokens_transfers_by_address) | **GET** /blockchain-data/{blockchain}/{network}/addresses/{address}/tokens-transfers-unconfirmed | List Unconfirmed Tokens Transfers By Address


# **get_token_details_by_contract_address**
> GetTokenDetailsByContractAddressR get_token_details_by_contract_address(network, contract_address)

Get Token Details by Contract Address

Though this endpoint customers can obtain information about token details. This can be done by providing the `contact address` parameter.    {note}This address is **not** the same as the smart contract creator address.{/note}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import tokens_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.get_token_details_by_contract_address400_response import GetTokenDetailsByContractAddress400Response
from cryptoapis.model.get_token_details_by_contract_address403_response import GetTokenDetailsByContractAddress403Response
from cryptoapis.model.get_token_details_by_contract_address401_response import GetTokenDetailsByContractAddress401Response
from cryptoapis.model.get_token_details_by_contract_address_r import GetTokenDetailsByContractAddressR
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
    api_instance = tokens_api.TokensApi(api_client)
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    contract_address = "0x7495fede000c8a3b77eeae09cf70fa94cd2d53f5" # str | Defines the specific address of the contract.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Token Details by Contract Address
        api_response = api_instance.get_token_details_by_contract_address(network, contract_address)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TokensApi->get_token_details_by_contract_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Token Details by Contract Address
        api_response = api_instance.get_token_details_by_contract_address(network, contract_address, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TokensApi->get_token_details_by_contract_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **contract_address** | **str**| Defines the specific address of the contract. |
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | defaults to "ethereum"
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**GetTokenDetailsByContractAddressR**](GetTokenDetailsByContractAddressR.md)

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

# **list_confirmed_tokens_transfers_by_address**
> ListConfirmedTokensTransfersByAddressR list_confirmed_tokens_transfers_by_address(blockchain, network, address)

List Confirmed Tokens Transfers By Address

Through this endpoint customers can obtain a list with **confirmed** token transfers by the `address` attribute. Token transfers may include information such as addresses of the sender and recipient, token name, token symbol, etc.    {note}This refers only to transfers done for **confirmed tokens** not coins.{/note}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import tokens_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.list_confirmed_tokens_transfers_by_address_r import ListConfirmedTokensTransfersByAddressR
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.list_confirmed_tokens_transfers_by_address400_response import ListConfirmedTokensTransfersByAddress400Response
from cryptoapis.model.list_confirmed_tokens_transfers_by_address403_response import ListConfirmedTokensTransfersByAddress403Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.convert_bitcoin_cash_address409_response import ConvertBitcoinCashAddress409Response
from cryptoapis.model.list_confirmed_tokens_transfers_by_address401_response import ListConfirmedTokensTransfersByAddress401Response
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
    api_instance = tokens_api.TokensApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Ethereum Classic, etc.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    address = "0x033ef6db9fbd0ee60e2931906b987fe0280471a0" # str | Represents the public address, which is a compressed and shortened form of a public key.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Confirmed Tokens Transfers By Address
        api_response = api_instance.list_confirmed_tokens_transfers_by_address(blockchain, network, address)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TokensApi->list_confirmed_tokens_transfers_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Confirmed Tokens Transfers By Address
        api_response = api_instance.list_confirmed_tokens_transfers_by_address(blockchain, network, address, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TokensApi->list_confirmed_tokens_transfers_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Ethereum Classic, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **address** | **str**| Represents the public address, which is a compressed and shortened form of a public key. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListConfirmedTokensTransfersByAddressR**](ListConfirmedTokensTransfersByAddressR.md)

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

# **list_tokens_by_address**
> ListTokensByAddressR list_tokens_by_address(blockchain, network, address)

List Tokens By Address

Through this endpoint customers can obtain token data by providing an attribute - `address`.  The information that can be returned can include the contract address, the token symbol, type and balance.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import tokens_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.list_tokens_by_address_r import ListTokensByAddressR
from cryptoapis.model.list_tokens_by_address403_response import ListTokensByAddress403Response
from cryptoapis.model.list_tokens_by_address401_response import ListTokensByAddress401Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.convert_bitcoin_cash_address409_response import ConvertBitcoinCashAddress409Response
from cryptoapis.model.list_tokens_by_address400_response import ListTokensByAddress400Response
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
    api_instance = tokens_api.TokensApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Ethereum Classic, etc.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    address = "0x033ef6db9fbd0ee60e2931906b987fe0280471a0" # str | Represents the public address, which is a compressed and shortened form of a public key.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Tokens By Address
        api_response = api_instance.list_tokens_by_address(blockchain, network, address)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TokensApi->list_tokens_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Tokens By Address
        api_response = api_instance.list_tokens_by_address(blockchain, network, address, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TokensApi->list_tokens_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Ethereum Classic, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **address** | **str**| Represents the public address, which is a compressed and shortened form of a public key. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListTokensByAddressR**](ListTokensByAddressR.md)

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

# **list_tokens_transfers_by_transaction_hash**
> ListTokensTransfersByTransactionHashR list_tokens_transfers_by_transaction_hash(blockchain, network, transaction_hash)

List Tokens Transfers By Transaction Hash

Through this endpoint customers can obtain a list with token transfers by the `transactionHash` attribute. Token transfers may include information such as addresses of the sender and recipient, token name, token symbol, etc.    {note}This refers only to transfers done for **tokens** not coins.{/note}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import tokens_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.list_tokens_transfers_by_transaction_hash403_response import ListTokensTransfersByTransactionHash403Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.list_tokens_transfers_by_transaction_hash400_response import ListTokensTransfersByTransactionHash400Response
from cryptoapis.model.list_tokens_transfers_by_transaction_hash_r import ListTokensTransfersByTransactionHashR
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.convert_bitcoin_cash_address409_response import ConvertBitcoinCashAddress409Response
from cryptoapis.model.list_tokens_transfers_by_transaction_hash401_response import ListTokensTransfersByTransactionHash401Response
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
    api_instance = tokens_api.TokensApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Ethereum Classic, etc.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    transaction_hash = "0xbe38781783b1b9d480219255ff98e20335a39e13979a66112efa33f05fde0a33" # str | Represents the hash of the transaction, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Tokens Transfers By Transaction Hash
        api_response = api_instance.list_tokens_transfers_by_transaction_hash(blockchain, network, transaction_hash)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TokensApi->list_tokens_transfers_by_transaction_hash: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Tokens Transfers By Transaction Hash
        api_response = api_instance.list_tokens_transfers_by_transaction_hash(blockchain, network, transaction_hash, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TokensApi->list_tokens_transfers_by_transaction_hash: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Ethereum Classic, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **transaction_hash** | **str**| Represents the hash of the transaction, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListTokensTransfersByTransactionHashR**](ListTokensTransfersByTransactionHashR.md)

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

# **list_unconfirmed_tokens_transfers_by_address**
> ListUnconfirmedTokensTransfersByAddressR list_unconfirmed_tokens_transfers_by_address(blockchain, network, address)

List Unconfirmed Tokens Transfers By Address

Through this endpoint customers can obtain a list with **unconfirmed** token transfers by the `address` attribute. Token transfers may include information such as addresses of the sender and recipient, token name, token symbol, etc.    {note}This refers only to transfers done for **unconfirmed tokens** not coins.{/note}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import tokens_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.list_unconfirmed_tokens_transfers_by_address400_response import ListUnconfirmedTokensTransfersByAddress400Response
from cryptoapis.model.list_unconfirmed_tokens_transfers_by_address403_response import ListUnconfirmedTokensTransfersByAddress403Response
from cryptoapis.model.list_unconfirmed_tokens_transfers_by_address_r import ListUnconfirmedTokensTransfersByAddressR
from cryptoapis.model.list_unconfirmed_tokens_transfers_by_address401_response import ListUnconfirmedTokensTransfersByAddress401Response
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
    api_instance = tokens_api.TokensApi(api_client)
    blockchain = "ethereum" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Ethereum Classic, etc.
    network = "ropsten" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    address = "0x033ef6db9fbd0ee60e2931906b987fe0280471a0" # str | Represents the public address, which is a compressed and shortened form of a public key.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Unconfirmed Tokens Transfers By Address
        api_response = api_instance.list_unconfirmed_tokens_transfers_by_address(blockchain, network, address)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TokensApi->list_unconfirmed_tokens_transfers_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Unconfirmed Tokens Transfers By Address
        api_response = api_instance.list_unconfirmed_tokens_transfers_by_address(blockchain, network, address, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling TokensApi->list_unconfirmed_tokens_transfers_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Ethereum Classic, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **address** | **str**| Represents the public address, which is a compressed and shortened form of a public key. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **limit** | **int**| Defines how many items should be returned in the response per page basis. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The starting index of the response items, i.e. where the response should start listing the returned items. | [optional] if omitted the server will use the default value of 0

### Return type

[**ListUnconfirmedTokensTransfersByAddressR**](ListUnconfirmedTokensTransfersByAddressR.md)

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

