# CreateSingleTransactionRequestFromAddressWithoutFeePriorityRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient** | [**[CreateSingleTransactionRequestFromAddressWithoutFeePriorityRIRecipientInner]**](CreateSingleTransactionRequestFromAddressWithoutFeePriorityRIRecipientInner.md) | Defines the destination for the transaction, i.e. the recipient(s). | 
**sender** | [**CreateSingleTransactionRequestFromAddressWithoutFeePriorityRISender**](CreateSingleTransactionRequestFromAddressWithoutFeePriorityRISender.md) |  | 
**transaction_request_id** | **str** | Represents a unique identifier of the transaction request (the request sent to make a transaction), which helps in identifying which callback and which &#x60;referenceId&#x60; concern that specific transaction request. | 
**transaction_request_status** | **str** | Defines the status of the transaction, e.g. \&quot;created, \&quot;await_approval\&quot;, \&quot;pending\&quot;, \&quot;prepared\&quot;, \&quot;signed\&quot;, \&quot;broadcasted\&quot;, \&quot;success\&quot;, \&quot;failed\&quot;, \&quot;rejected\&quot;, mined\&quot;. | 
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security). | [optional] 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. &#x60;We support ONLY httpS type of protocol&#x60;. | [optional] 
**classic_address** | **str** | Represents the public address, which is a compressed and shortened form of a public key. The classic address is shown when the source address is an x-Address. | [optional] 
**note** | **str** | Represents an optional note to add a free text in, explaining or providing additional detail on the transaction request. | [optional] 
**total_amount** | [**CreateSingleTransactionRequestFromAddressWithoutFeePriorityRITotalAmount**](CreateSingleTransactionRequestFromAddressWithoutFeePriorityRITotalAmount.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


