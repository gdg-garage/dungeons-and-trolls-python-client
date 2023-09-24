# DungeonsandtrollsCharacter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**attributes** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**money** | **int** |  | [optional] 
**equip** | [**List[DungeonsandtrollsItem]**](DungeonsandtrollsItem.md) |  | [optional] 
**score** | **float** |  | [optional] 
**skill_points** | **float** |  | [optional] 
**effects** | [**List[DungeonsandtrollsEffect]**](DungeonsandtrollsEffect.md) |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_character import DungeonsandtrollsCharacter

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsCharacter from a JSON string
dungeonsandtrolls_character_instance = DungeonsandtrollsCharacter.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsCharacter.to_json()

# convert the object into a dict
dungeonsandtrolls_character_dict = dungeonsandtrolls_character_instance.to_dict()
# create an instance of DungeonsandtrollsCharacter from a dict
dungeonsandtrolls_character_form_dict = dungeonsandtrolls_character.from_dict(dungeonsandtrolls_character_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


