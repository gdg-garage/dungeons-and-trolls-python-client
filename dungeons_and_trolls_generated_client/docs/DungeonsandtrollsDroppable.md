# DungeonsandtrollsDroppable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skill** | [**DungeonsandtrollsSkill**](DungeonsandtrollsSkill.md) |  | [optional] 
**item** | [**DungeonsandtrollsItem**](DungeonsandtrollsItem.md) |  | [optional] 
**monster** | [**DungeonsandtrollsMonster**](DungeonsandtrollsMonster.md) |  | [optional] 
**decoration** | [**DungeonsandtrollsDecoration**](DungeonsandtrollsDecoration.md) |  | [optional] 
**waypoint** | [**DungeonsandtrollsWaypoint**](DungeonsandtrollsWaypoint.md) |  | [optional] 
**key** | [**DungeonsandtrollsKey**](DungeonsandtrollsKey.md) |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_droppable import DungeonsandtrollsDroppable

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsDroppable from a JSON string
dungeonsandtrolls_droppable_instance = DungeonsandtrollsDroppable.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsDroppable.to_json()

# convert the object into a dict
dungeonsandtrolls_droppable_dict = dungeonsandtrolls_droppable_instance.to_dict()
# create an instance of DungeonsandtrollsDroppable from a dict
dungeonsandtrolls_droppable_form_dict = dungeonsandtrolls_droppable.from_dict(dungeonsandtrolls_droppable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


