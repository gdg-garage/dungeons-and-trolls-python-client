# DungeonsandtrollsCoordinates


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **int** |  | [optional] 
**position_x** | **int** |  | [optional] 
**position_y** | **int** |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_coordinates import DungeonsandtrollsCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsCoordinates from a JSON string
dungeonsandtrolls_coordinates_instance = DungeonsandtrollsCoordinates.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsCoordinates.to_json()

# convert the object into a dict
dungeonsandtrolls_coordinates_dict = dungeonsandtrolls_coordinates_instance.to_dict()
# create an instance of DungeonsandtrollsCoordinates from a dict
dungeonsandtrolls_coordinates_form_dict = dungeonsandtrolls_coordinates.from_dict(dungeonsandtrolls_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


