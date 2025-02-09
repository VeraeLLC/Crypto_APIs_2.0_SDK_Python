# GetBlockDetailsByBlockHeightRIBS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**difficulty** | **str** | Represents a mathematical value of how hard it is to find a valid hash for this block. | [optional] 
**bits** | **str** | Represents a specific sub-unit of Zcash. Bits have two-decimal precision | [optional] 
**chainwork** | **str** | Represents a hexadecimal number of all the hashes necessary to produce the current chain. E.g., when converting 0000000000000000000000000000000000000000000086859f7a841475b236fd to a decimal you get 635262017308958427068157 hashes, or 635262 exahashes. | [optional] 
**merkle_root** | **str** | Defines the single and final (root) node of a Merkle tree. It is the combined hash of all transactions&#39; hashes that are part of a blockchain block. | [optional] 
**nonce** | **str** | Represents a random value that can be adjusted to satisfy the Proof of Work. | [optional] 
**size** | **int** | Represents the total size of the block in Bytes. | [optional] 
**stripped_size** | **int** | Defines the numeric representation of the block size excluding the witness data. | [optional] 
**version** | **int** | Represents the block version number. | [optional] 
**version_hex** | **str** | Is the hexadecimal string representation of the block&#39;s version. | [optional] 
**weight** | **int** | Represents a measurement to compare the size of different transactions to each other in proportion to the block size limi | [optional] 
**extra_data** | **str** | Represents any data that can be included by the miner in the block. | [optional] 
**gas_limit** | **int** | Numeric representation of the block gas_limit | [optional] 
**gas_used** | **int** | Numeric representation of the block gas_limit | [optional] 
**mined_in_seconds** | **int** | Specifies the amount of time required for the block to be mined in seconds. | [optional] 
**sha3_uncles** | **str** | Defines the combined hash of all uncles for a given parent. | [optional] 
**total_difficulty** | **str** | Defines the total difficulty of the chain until this block, i.e. how difficult it is for a specific miner to mine a new block. | [optional] 
**ds_block** | **int** | Numeric representation of the ds block | [optional] 
**ds_difficulty** | **str** | Numeric representation of the ds difficulty | [optional] 
**ds_leader** | **str** | String representation of the ds leader | [optional] 
**micro_blocks** | **[str]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


