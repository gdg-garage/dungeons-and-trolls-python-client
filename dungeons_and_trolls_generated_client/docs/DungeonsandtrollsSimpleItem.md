# DungeonsandtrollsSimpleItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**slot** | [**DungeonsandtrollsItemType**](DungeonsandtrollsItemType.md) |  | [optional] 
**icon** | **str** |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_simple_item import DungeonsandtrollsSimpleItem

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsSimpleItem from a JSON string
dungeonsandtrolls_simple_item_instance = DungeonsandtrollsSimpleItem.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsSimpleItem.to_json()

# convert the object into a dict
dungeonsandtrolls_simple_item_dict = dungeonsandtrolls_simple_item_instance.to_dict()
# create an instance of DungeonsandtrollsSimpleItem from a dict
dungeonsandtrolls_simple_item_form_dict = dungeonsandtrolls_simple_item.from_dict(dungeonsandtrolls_simple_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


