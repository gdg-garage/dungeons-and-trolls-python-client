# DungeonsandtrollsEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**type** | [**DungeonsandtrollsEventType**](DungeonsandtrollsEventType.md) |  | [optional] 
**coordinates** | [**DungeonsandtrollsCoordinates**](DungeonsandtrollsCoordinates.md) |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_event import DungeonsandtrollsEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsEvent from a JSON string
dungeonsandtrolls_event_instance = DungeonsandtrollsEvent.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsEvent.to_json()

# convert the object into a dict
dungeonsandtrolls_event_dict = dungeonsandtrolls_event_instance.to_dict()
# create an instance of DungeonsandtrollsEvent from a dict
dungeonsandtrolls_event_form_dict = dungeonsandtrolls_event.from_dict(dungeonsandtrolls_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


