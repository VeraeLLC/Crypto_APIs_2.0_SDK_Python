# ListConfirmedTransactionsByAddressRIBS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid. | [optional] 
**size** | **int** | Represents the total size of this transaction. | [optional] 
**v_size** | **int** | Represents the virtual size of this transaction. | [optional] 
**version** | **int** | Defines the version of the transaction. | [optional] 
**vin** | [**[ListConfirmedTransactionsByAddressRIBSZVinInner]**](ListConfirmedTransactionsByAddressRIBSZVinInner.md) | Object Array representation of transaction inputs | [optional] 
**vout** | [**[GetTransactionDetailsByTransactionIDRIBSZVoutInner]**](GetTransactionDetailsByTransactionIDRIBSZVoutInner.md) | Object Array representation of transaction outputs | [optional] 
**contract** | **str** | Represents the specific transaction contract. | [optional] 
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | [optional] 
**gas_price** | [**ListConfirmedTransactionsByAddressRIBSBSCGasPrice**](ListConfirmedTransactionsByAddressRIBSBSCGasPrice.md) |  | [optional] 
**gas_used** | **str** | Represents the exact unit of gas that was used for the transaction. | [optional] 
**input_data** | **str** | Represents additional information that is required for the transaction. | [optional] 
**internal_transactions_count** | **int** | Represents the total internal transactions count. | [optional] 
**nonce** | **int** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | [optional] 
**token_transfers_count** | **int** | Represents the total token transfers count. | [optional] 
**transaction_status** | **str** | String representation of the transaction status | [optional] 
**binding_sig** | **str** | It is used to enforce balance of Spend and Output transfers, in order to prevent their replay across transactions. | [optional] 
**expiry_height** | **int** | Represents a block height after which the transaction will expire. | [optional] 
**join_split_pub_key** | **str** | Represents an encoding of a JoinSplitSig public validating key. | [optional] 
**join_split_sig** | **str** | Is used to sign transactions that contain at least one JoinSplit description. | [optional] 
**overwintered** | **bool** | \&quot;Overwinter\&quot; is the network upgrade for the Zcash blockchain. | [optional] 
**v_join_split** | [**[ListConfirmedTransactionsByAddressRIBSZVJoinSplitInner]**](ListConfirmedTransactionsByAddressRIBSZVJoinSplitInner.md) | Represents a sequence of JoinSplit descriptions using BCTV14 proofs. | [optional] 
**v_shielded_output** | [**[GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner.md) | Object Array representation of transaction output descriptions | [optional] 
**v_shielded_spend** | [**[GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner.md) | Object Array representation of transaction spend descriptions | [optional] 
**value_balance** | **str** | Defines the transaction value balance. | [optional] 
**version_group_id** | **str** | Represents the transaction version group ID. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


