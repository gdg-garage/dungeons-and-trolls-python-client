# DungeonsandtrollsMonster


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**items** | [**List[DungeonsandtrollsSimpleItem]**](DungeonsandtrollsSimpleItem.md) |  | [optional] 
**effects** | [**List[DungeonsandtrollsEffect]**](DungeonsandtrollsEffect.md) |  | [optional] 
**life_percentage** | **float** |  | [optional] 
**faction** | **str** |  | [optional] 
**attributes** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**equipped_items** | [**List[DungeonsandtrollsItem]**](DungeonsandtrollsItem.md) |  | [optional] 
**score** | **float** |  | [optional] 
**algorithm** | **str** |  | [optional] 
**on_death** | [**List[DungeonsandtrollsDroppable]**](DungeonsandtrollsDroppable.md) |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_monster import DungeonsandtrollsMonster

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsMonster from a JSON string
dungeonsandtrolls_monster_instance = DungeonsandtrollsMonster.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsMonster.to_json()

# convert the object into a dict
dungeonsandtrolls_monster_dict = dungeonsandtrolls_monster_instance.to_dict()
# create an instance of DungeonsandtrollsMonster from a dict
dungeonsandtrolls_monster_form_dict = dungeonsandtrolls_monster.from_dict(dungeonsandtrolls_monster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


