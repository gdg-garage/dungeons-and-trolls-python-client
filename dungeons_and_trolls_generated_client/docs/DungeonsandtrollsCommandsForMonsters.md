# DungeonsandtrollsCommandsForMonsters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commands** | [**Dict[str, DungeonsandtrollsCommandsBatch]**](DungeonsandtrollsCommandsBatch.md) | Monster ID with corresponding batch of commands. | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_commands_for_monsters import DungeonsandtrollsCommandsForMonsters

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsCommandsForMonsters from a JSON string
dungeonsandtrolls_commands_for_monsters_instance = DungeonsandtrollsCommandsForMonsters.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsCommandsForMonsters.to_json()

# convert the object into a dict
dungeonsandtrolls_commands_for_monsters_dict = dungeonsandtrolls_commands_for_monsters_instance.to_dict()
# create an instance of DungeonsandtrollsCommandsForMonsters from a dict
dungeonsandtrolls_commands_for_monsters_form_dict = dungeonsandtrolls_commands_for_monsters.from_dict(dungeonsandtrolls_commands_for_monsters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


