# DungeonsandtrollsCommandsBatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buy** | [**DungeonsandtrollsIdentifiers**](DungeonsandtrollsIdentifiers.md) |  | [optional] 
**pick_up** | [**DungeonsandtrollsIdentifier**](DungeonsandtrollsIdentifier.md) |  | [optional] 
**move** | [**DungeonsandtrollsPosition**](DungeonsandtrollsPosition.md) |  | [optional] 
**skill** | [**DungeonsandtrollsSkillUse**](DungeonsandtrollsSkillUse.md) |  | [optional] 
**yell** | [**DungeonsandtrollsMessage**](DungeonsandtrollsMessage.md) |  | [optional] 
**assign_skill_points** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_commands_batch import DungeonsandtrollsCommandsBatch

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsCommandsBatch from a JSON string
dungeonsandtrolls_commands_batch_instance = DungeonsandtrollsCommandsBatch.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsCommandsBatch.to_json()

# convert the object into a dict
dungeonsandtrolls_commands_batch_dict = dungeonsandtrolls_commands_batch_instance.to_dict()
# create an instance of DungeonsandtrollsCommandsBatch from a dict
dungeonsandtrolls_commands_batch_form_dict = dungeonsandtrolls_commands_batch.from_dict(dungeonsandtrolls_commands_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


