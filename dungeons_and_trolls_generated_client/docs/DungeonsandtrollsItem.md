# DungeonsandtrollsItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**slot** | [**DungeonsandtrollsItemType**](DungeonsandtrollsItemType.md) |  | [optional] 
**price** | **int** |  | [optional] 
**requirements** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**attributes** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**skills** | [**List[DungeonsandtrollsSkill]**](DungeonsandtrollsSkill.md) |  | [optional] 
**icon** | **str** |  | [optional] 
**unidentified** | **bool** |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_item import DungeonsandtrollsItem

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsItem from a JSON string
dungeonsandtrolls_item_instance = DungeonsandtrollsItem.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsItem.to_json()

# convert the object into a dict
dungeonsandtrolls_item_dict = dungeonsandtrolls_item_instance.to_dict()
# create an instance of DungeonsandtrollsItem from a dict
dungeonsandtrolls_item_form_dict = dungeonsandtrolls_item.from_dict(dungeonsandtrolls_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


