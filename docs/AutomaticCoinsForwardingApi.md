# cryptoapis.AutomaticCoinsForwardingApi

All URIs are relative to *https://rest.cryptoapis.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_automatic_coins_forwarding**](AutomaticCoinsForwardingApi.md#create_automatic_coins_forwarding) | **POST** /blockchain-automations/{blockchain}/{network}/coins-forwarding/automations | Create Automatic Coins Forwarding
[**delete_automatic_coins_forwarding**](AutomaticCoinsForwardingApi.md#delete_automatic_coins_forwarding) | **DELETE** /blockchain-automations/{blockchain}/{network}/coins-forwarding/automations/{referenceId} | Delete Automatic Coins Forwarding
[**list_coins_forwarding_automations**](AutomaticCoinsForwardingApi.md#list_coins_forwarding_automations) | **GET** /blockchain-automations/{blockchain}/{network}/coins-forwarding/automations | List Coins Forwarding Automations


# **create_automatic_coins_forwarding**
> CreateAutomaticCoinsForwardingR create_automatic_coins_forwarding(blockchain, network)

Create Automatic Coins Forwarding

Through this endpoint customers can set up an automatic forwarding function specifically for coins (**not** tokens). They can have a `toAddress` which is essentially the main address and the destination for the automatic coins forwarding.     There is also a `minimumTransferAmount` which only when reached will then trigger the forwarding. Through this the customer can save from fees.    Moreover, `feePriority` can be also set,  which defines how quickly to move the coins once they are received. The higher priority, the larger the fee will be. It can be \"SLOW\", \"STANDARD\" or \"FAST\".    The response of this endpoint contains an attribute `fromAddress` which can be used as a deposit address. Any funds received by this address will be automatically forwarded to `toAddress` based on what the customer has set for the automation.    For this automatic forwarding the customer can set a callback subscription.    {warning}The subscription will work for all incoming transactions until it is deleted. There is no need to do that for every transaction.{/warning}    {note}This endpoint generates a new `fromAddress` each time.{/note}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import automatic_coins_forwarding_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.create_automatic_coins_forwarding_r import CreateAutomaticCoinsForwardingR
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.create_automatic_coins_forwarding409_response import CreateAutomaticCoinsForwarding409Response
from cryptoapis.model.create_automatic_coins_forwarding401_response import CreateAutomaticCoinsForwarding401Response
from cryptoapis.model.get_xrp_ripple_transaction_details_by_transaction_id404_response import GetXRPRippleTransactionDetailsByTransactionID404Response
from cryptoapis.model.create_automatic_coins_forwarding_rb import CreateAutomaticCoinsForwardingRB
from cryptoapis.model.create_automatic_coins_forwarding400_response import CreateAutomaticCoinsForwarding400Response
from cryptoapis.model.create_automatic_coins_forwarding403_response import CreateAutomaticCoinsForwarding403Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
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
    api_instance = automatic_coins_forwarding_api.AutomaticCoinsForwardingApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    create_automatic_coins_forwarding_rb = CreateAutomaticCoinsForwardingRB(
        context="yourExampleString",
        data=CreateAutomaticCoinsForwardingRBData(
            item=CreateAutomaticCoinsForwardingRBDataItem(
                callback_secret_key="yourSecretString",
                callback_url="https://example.com",
                confirmations_count=3,
                fee_priority="standard",
                minimum_transfer_amount="0.02",
                to_address="mzYijhgmzZrmuB7wBDazRKirnChKyow4M3",
            ),
        ),
    ) # CreateAutomaticCoinsForwardingRB |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Automatic Coins Forwarding
        api_response = api_instance.create_automatic_coins_forwarding(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AutomaticCoinsForwardingApi->create_automatic_coins_forwarding: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Automatic Coins Forwarding
        api_response = api_instance.create_automatic_coins_forwarding(blockchain, network, context=context, create_automatic_coins_forwarding_rb=create_automatic_coins_forwarding_rb)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AutomaticCoinsForwardingApi->create_automatic_coins_forwarding: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]
 **create_automatic_coins_forwarding_rb** | [**CreateAutomaticCoinsForwardingRB**](CreateAutomaticCoinsForwardingRB.md)|  | [optional]

### Return type

[**CreateAutomaticCoinsForwardingR**](CreateAutomaticCoinsForwardingR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The resource has been successfully created. |  -  |
**400** | 400 |  -  |
**401** | 401 |  -  |
**402** | You have insufficient credits. Please upgrade your plan from your Dashboard or contact our team via email. |  -  |
**403** | 403 |  -  |
**404** | The specified resource has not been found. |  -  |
**409** | 409 |  -  |
**415** | The selected Media Type is unavailable. The Content-Type header should be &#39;application/json&#39;. |  -  |
**422** | Your request body for POST requests must have a structure of { data: { item: [...properties] } } |  -  |
**429** | The request limit has been reached. There can be maximum {requests} requests per {seconds} second(s) made. Please contact our team via email if you need more or upgrade your plan. |  -  |
**500** | An unexpected server error has occurred, we are working to fix this. Please try again later and in case it occurs again please report it to our team via email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_automatic_coins_forwarding**
> DeleteAutomaticCoinsForwardingR delete_automatic_coins_forwarding(blockchain, network, reference_id)

Delete Automatic Coins Forwarding

Through this endpoint customers can delete a forwarding function they have set for **coins** (**not** tokens).    By setting a `fromAddress` and a `toAddress`, and specifying the amount, coins can be transferred between addresses.     A `feePriority` will be returned which represents the fee priority of the automation whether it is \"SLOW\", \"STANDARD\" OR \"FAST\".    {warning}The subscription will work for all incoming transactions until it is deleted. There is no need to do that for every transaction.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import automatic_coins_forwarding_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.delete_automatic_coins_forwarding401_response import DeleteAutomaticCoinsForwarding401Response
from cryptoapis.model.get_xrp_ripple_transaction_details_by_transaction_id404_response import GetXRPRippleTransactionDetailsByTransactionID404Response
from cryptoapis.model.delete_automatic_coins_forwarding_r import DeleteAutomaticCoinsForwardingR
from cryptoapis.model.delete_automatic_coins_forwarding400_response import DeleteAutomaticCoinsForwarding400Response
from cryptoapis.model.delete_automatic_coins_forwarding403_response import DeleteAutomaticCoinsForwarding403Response
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
    api_instance = automatic_coins_forwarding_api.AutomaticCoinsForwardingApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    reference_id = "600955ea5e75d660e71d3c7d" # str | Represents a unique ID used to reference the specific callback subscription.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Automatic Coins Forwarding
        api_response = api_instance.delete_automatic_coins_forwarding(blockchain, network, reference_id)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AutomaticCoinsForwardingApi->delete_automatic_coins_forwarding: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Automatic Coins Forwarding
        api_response = api_instance.delete_automatic_coins_forwarding(blockchain, network, reference_id, context=context)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AutomaticCoinsForwardingApi->delete_automatic_coins_forwarding: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **str**| Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. |
 **network** | **str**| Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. |
 **reference_id** | **str**| Represents a unique ID used to reference the specific callback subscription. |
 **context** | **str**| In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional]

### Return type

[**DeleteAutomaticCoinsForwardingR**](DeleteAutomaticCoinsForwardingR.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The delete request has been successful. |  -  |
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

# **list_coins_forwarding_automations**
> ListCoinsForwardingAutomationsR list_coins_forwarding_automations(blockchain, network)

List Coins Forwarding Automations

Through this endpoint customers can list all of their **coins** forwarding automations (**not** tokens).    Customers can set up automatic forwarding functions for coins by setting a `fromAddress` and a `toAddress`, and specifying the amount that can be transferred between addresses.     A `feePriority` will be returned which represents the fee priority of the automation whether it is \"SLOW\", \"STANDARD\" OR \"FAST\".    {warning}The subscription will work for all transactions until it is deleted. There is no need to do that for every transaction.{/warning}

### Example

* Api Key Authentication (ApiKey):

```python
import time
import cryptoapis
from cryptoapis.api import automatic_coins_forwarding_api
from cryptoapis.model.convert_bitcoin_cash_address429_response import ConvertBitcoinCashAddress429Response
from cryptoapis.model.convert_bitcoin_cash_address500_response import ConvertBitcoinCashAddress500Response
from cryptoapis.model.convert_bitcoin_cash_address422_response import ConvertBitcoinCashAddress422Response
from cryptoapis.model.list_coins_forwarding_automations403_response import ListCoinsForwardingAutomations403Response
from cryptoapis.model.get_xrp_ripple_transaction_details_by_transaction_id404_response import GetXRPRippleTransactionDetailsByTransactionID404Response
from cryptoapis.model.list_coins_forwarding_automations400_response import ListCoinsForwardingAutomations400Response
from cryptoapis.model.list_coins_forwarding_automations401_response import ListCoinsForwardingAutomations401Response
from cryptoapis.model.convert_bitcoin_cash_address402_response import ConvertBitcoinCashAddress402Response
from cryptoapis.model.list_coins_forwarding_automations_r import ListCoinsForwardingAutomationsR
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
    api_instance = automatic_coins_forwarding_api.AutomaticCoinsForwardingApi(api_client)
    blockchain = "bitcoin" # str | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
    network = "testnet" # str | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\" are test networks.
    context = "yourExampleString" # str | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user. (optional)
    limit = 50 # int | Defines how many items should be returned in the response per page basis. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | The starting index of the response items, i.e. where the response should start listing the returned items. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List Coins Forwarding Automations
        api_response = api_instance.list_coins_forwarding_automations(blockchain, network)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AutomaticCoinsForwardingApi->list_coins_forwarding_automations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Coins Forwarding Automations
        api_response = api_instance.list_coins_forwarding_automations(blockchain, network, context=context, limit=limit, offset=offset)
        pprint(api_response)
    except cryptoapis.ApiException as e:
        print("Exception when calling AutomaticCoinsForwardingApi->list_coins_forwarding_automations: %s\n" % e)
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

[**ListCoinsForwardingAutomationsR**](ListCoinsForwardingAutomationsR.md)

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

