# DungeonsandtrollsGameState


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map** | [**DungeonsandtrollsMap**](DungeonsandtrollsMap.md) |  | [optional] 
**shop_items** | [**List[DungeonsandtrollsItem]**](DungeonsandtrollsItem.md) |  | [optional] 
**character** | [**DungeonsandtrollsCharacter**](DungeonsandtrollsCharacter.md) |  | [optional] 
**current_position** | [**DungeonsandtrollsPosition**](DungeonsandtrollsPosition.md) |  | [optional] 
**current_level** | **int** |  | [optional] 
**tick** | **int** |  | [optional] 
**events** | [**List[DungeonsandtrollsEvent]**](DungeonsandtrollsEvent.md) | List of events which occurred in the previous tick. Useful for visualising effects, debugging and communication. | [optional] 
**score** | **float** |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_game_state import DungeonsandtrollsGameState

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsGameState from a JSON string
dungeonsandtrolls_game_state_instance = DungeonsandtrollsGameState.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsGameState.to_json()

# convert the object into a dict
dungeonsandtrolls_game_state_dict = dungeonsandtrolls_game_state_instance.to_dict()
# create an instance of DungeonsandtrollsGameState from a dict
dungeonsandtrolls_game_state_form_dict = dungeonsandtrolls_game_state.from_dict(dungeonsandtrolls_game_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


