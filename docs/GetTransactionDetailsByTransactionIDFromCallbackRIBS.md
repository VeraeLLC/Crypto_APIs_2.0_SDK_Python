# GetTransactionDetailsByTransactionIDFromCallbackRIBS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_tag** | **int** | Defines the destination tag value. | [optional] 
**locktime** | **int** | Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid. | [optional] 
**size** | **int** | Represents the total size of this transaction. | [optional] 
**v_size** | **int** | Represents the virtual size of this transaction. | [optional] 
**version** | **int** | Defines the version of the transaction. | [optional] 
**vin** | [**[GetTransactionDetailsByTransactionIDRIBSZVinInner]**](GetTransactionDetailsByTransactionIDRIBSZVinInner.md) | Object Array representation of transaction inputs | [optional] 
**vout** | [**[GetTransactionDetailsByTransactionIDFromCallbackRIBSZVoutInner]**](GetTransactionDetailsByTransactionIDFromCallbackRIBSZVoutInner.md) | Object Array representation of transaction outputs | [optional] 
**contract** | **str** | Represents the specific transaction contract. | [optional] 
**gas_limit** | **int** | Represents the maximum amount of gas allowed in the block in order to determine how many transactions it can fit. | [optional] 
**gas_price** | **str** | Represents the price offered to the miner to purchase this amount of gas. | [optional] 
**gas_used** | **str** | Represents the exact unit of gas that was used for the transaction. | [optional] 
**input_data** | **str** | Represents additional information that is required for the transaction. | [optional] 
**nonce** | **int** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | [optional] 
**transaction_status** | **str** | Represents the status of this transaction. | [optional] 
**binding_sig** | **str** | It is used to enforce balance of Spend and Output transfers, in order to prevent their replay across transactions. | [optional] 
**expiry_height** | **int** | Represents a block height after which the transaction will expire. | [optional] 
**join_split_pub_key** | **str** | Represents an encoding of a JoinSplitSig public validating key. | [optional] 
**join_split_sig** | **str** | Is used to sign transactions that contain at least one JoinSplit description. | [optional] 
**overwintered** | **bool** | \&quot;Overwinter\&quot; is the network upgrade for the Zcash blockchain. | [optional] 
**v_join_split** | [**[GetTransactionDetailsByTransactionIDRIBSZVJoinSplitInner]**](GetTransactionDetailsByTransactionIDRIBSZVJoinSplitInner.md) | Represents a sequence of JoinSplit descriptions using BCTV14 proofs. | [optional] 
**v_shielded_output** | [**[GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedOutputInner.md) | Object Array representation of transaction output descriptions | [optional] 
**v_shielded_spend** | [**[GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner.md) | Object Array representation of transaction spend descriptions | [optional] 
**value_balance** | **str** | String representation of the transaction value balance | [optional] 
**version_group_id** | **str** | Represents the transaction version group ID | [optional] 
**additional_data** | **str** | Represents additional data that may be needed. | [optional] 
**offer** | [**GetXRPRippleTransactionDetailsByTransactionIDRIOffer**](GetXRPRippleTransactionDetailsByTransactionIDRIOffer.md) |  | [optional] 
**receive** | [**GetXRPRippleTransactionDetailsByTransactionIDRIReceive**](GetXRPRippleTransactionDetailsByTransactionIDRIReceive.md) |  | [optional] 
**sequence** | **int** | Defines the transaction input&#39;s sequence as an integer, which is is used when transactions are replaced with newer versions before LockTime. | [optional] 
**status** | **str** | Defines the status of the transaction. | [optional] 
**type** | **str** | Defines the type of the transaction. | [optional] 
**value** | [**GetTransactionDetailsByTransactionIDFromCallbackRIBSXValue**](GetTransactionDetailsByTransactionIDFromCallbackRIBSXValue.md) |  | [optional] 
**amount** | **str** | Representation of the amount value. | [optional] 
**bandwidth_used** | [**GetTransactionDetailsByTransactionIDFromCallbackRIBSTBandwidthUsed**](GetTransactionDetailsByTransactionIDFromCallbackRIBSTBandwidthUsed.md) |  | [optional] 
**energy_used** | [**GetTransactionDetailsByTransactionIDFromCallbackRIBSTEnergyUsed**](GetTransactionDetailsByTransactionIDFromCallbackRIBSTEnergyUsed.md) |  | [optional] 
**has_internal_transactions** | **bool** | Defines if the transaction includes internal transactions (true) or not (false). | [optional] 
**has_token_transfers** | **str** | Defines if the transaction includes token transfers (true) or not (false). | [optional] 
**input** | **str** | Represents additional information that is required for the transaction. | [optional] 
**recipients** | **str** | Represents a list of recipient addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | [optional] 
**senders** | **str** | Represents a list of sender addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | [optional] 
**gas** | **str** | Represents the price offered to the miner to purchase this amount of gas. | [optional] 
**txid** | **str** | Represents the unique identifier of a transaction, i.e. it could be transactionId in UTXO-based protocols like Bitcoin, and transaction hash in Ethereum blockchain. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


