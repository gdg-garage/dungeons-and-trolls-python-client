# DungeonsandtrollsLevel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **int** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**free** | **List[List[object]]** |  | [optional] 
**objects** | [**List[DungeonsandtrollsMapObjects]**](DungeonsandtrollsMapObjects.md) |  | [optional] 
**ascii** | **List[str]** |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_level import DungeonsandtrollsLevel

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsLevel from a JSON string
dungeonsandtrolls_level_instance = DungeonsandtrollsLevel.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsLevel.to_json()

# convert the object into a dict
dungeonsandtrolls_level_dict = dungeonsandtrolls_level_instance.to_dict()
# create an instance of DungeonsandtrollsLevel from a dict
dungeonsandtrolls_level_form_dict = dungeonsandtrolls_level.from_dict(dungeonsandtrolls_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


