# GetWalletTransactionDetailsByTransactionIDRIBS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v_join_split** | [**[GetTransactionDetailsByTransactionIDRIBSZVJoinSplitInner]**](GetTransactionDetailsByTransactionIDRIBSZVJoinSplitInner.md) | Represents a sequence of JoinSplit descriptions using BCTV14 proofs. | [optional] 
**v_shielded_output** | [**[GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner.md) | Object Array representation of transaction output descriptions | [optional] 
**v_shielded_spend** | [**[GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner.md) | Object Array representation of transaction spend descriptions | [optional] 
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | [optional] 
**size** | **int** | Represents the total size of this transaction. | [optional] 
**v_size** | **int** | Represents the virtual size of this transaction. | [optional] 
**version** | **int** | Represents the transaction version number. | [optional] 
**vin** | [**[GetWalletTransactionDetailsByTransactionIDRIBSZVinInner]**](GetWalletTransactionDetailsByTransactionIDRIBSZVinInner.md) | Object Array representation of transaction inputs | [optional] 
**vout** | [**[ListTransactionsByBlockHeightRIBSZVoutInner]**](ListTransactionsByBlockHeightRIBSZVoutInner.md) | Object Array representation of transaction outputs | [optional] 
**contract** | **str** | Represents the specific transaction contract | [optional] 
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | [optional] 
**gas_price** | [**GetWalletTransactionDetailsByTransactionIDRIBSPGasPrice**](GetWalletTransactionDetailsByTransactionIDRIBSPGasPrice.md) |  | [optional] 
**gas_used** | **str** | Defines the unit of the gas price amount, e.g. BTC, ETH, XRP. | [optional] 
**input_data** | **str** | Represents additional information that is required for the transaction. | [optional] 
**nonce** | **int** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | [optional] 
**transaction_status** | **str** | String representation of the transaction status | [optional] 
**binding_sig** | **str** | It is used to enforce balance of Spend and Output transfers, in order to prevent their replay across transactions. | [optional] 
**expiry_height** | **int** | Represents a block height after which the transaction will expire. | [optional] 
**join_split_pub_key** | **str** | Represents an encoding of a JoinSplitSig public validating key. | [optional] 
**join_split_sig** | **str** | Is used to sign transactions that contain at least one JoinSplit description. | [optional] 
**overwintered** | **bool** | \&quot;Overwinter\&quot; is the network upgrade for the Zcash blockchain. | [optional] 
**value_balance** | **str** | String representation of the transaction value balance | [optional] 
**version_group_id** | **str** | Represents the transaction version group ID. | [optional] 
**amount** | **str** | String representation of the amount value | [optional] 
**bandwidth_used** | **str** | Numeric representation of the transaction used bandwidth | [optional] 
**energy_used** | **str** | String representation of the transaction used energy | [optional] 
**has_internal_transactions** | **bool** |  | [optional] 
**has_token_transfers** | **bool** |  | [optional] 
**input** | **str** | Numeric representation of the transaction input | [optional] 
**status** | **str** | String representation of the transaction status | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


