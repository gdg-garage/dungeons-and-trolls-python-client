# DungeonsandtrollsMapObjects


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | [**DungeonsandtrollsPosition**](DungeonsandtrollsPosition.md) |  | [optional] 
**monsters** | [**List[DungeonsandtrollsMonster]**](DungeonsandtrollsMonster.md) |  | [optional] 
**players** | [**List[DungeonsandtrollsCharacter]**](DungeonsandtrollsCharacter.md) |  | [optional] 
**is_stairs** | **bool** |  | [optional] 
**portal** | [**DungeonsandtrollsWaypoint**](DungeonsandtrollsWaypoint.md) |  | [optional] 
**decorations** | [**List[DungeonsandtrollsDecoration]**](DungeonsandtrollsDecoration.md) |  | [optional] 
**effects** | [**List[DungeonsandtrollsEffect]**](DungeonsandtrollsEffect.md) |  | [optional] 
**items** | [**List[DungeonsandtrollsItem]**](DungeonsandtrollsItem.md) |  | [optional] 
**is_free** | **bool** |  | [optional] 
**is_wall** | **bool** |  | [optional] 
**is_door** | **bool** |  | [optional] 
**is_spawn** | **bool** |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_map_objects import DungeonsandtrollsMapObjects

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsMapObjects from a JSON string
dungeonsandtrolls_map_objects_instance = DungeonsandtrollsMapObjects.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsMapObjects.to_json()

# convert the object into a dict
dungeonsandtrolls_map_objects_dict = dungeonsandtrolls_map_objects_instance.to_dict()
# create an instance of DungeonsandtrollsMapObjects from a dict
dungeonsandtrolls_map_objects_form_dict = dungeonsandtrolls_map_objects.from_dict(dungeonsandtrolls_map_objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


