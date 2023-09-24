# DungeonsandtrollsMap


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**levels** | [**List[DungeonsandtrollsLevel]**](DungeonsandtrollsLevel.md) |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_map import DungeonsandtrollsMap

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsMap from a JSON string
dungeonsandtrolls_map_instance = DungeonsandtrollsMap.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsMap.to_json()

# convert the object into a dict
dungeonsandtrolls_map_dict = dungeonsandtrolls_map_instance.to_dict()
# create an instance of DungeonsandtrollsMap from a dict
dungeonsandtrolls_map_form_dict = dungeonsandtrolls_map.from_dict(dungeonsandtrolls_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


