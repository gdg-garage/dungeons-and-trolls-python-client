# DungeonsandtrollsEffect


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**damage_amount** | **float** |  | [optional] 
**damage_type** | [**DungeonsandtrollsDamageType**](DungeonsandtrollsDamageType.md) |  | [optional] 
**effects** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**duration** | **int** |  | [optional] 
**caster_id** | **str** |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_effect import DungeonsandtrollsEffect

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsEffect from a JSON string
dungeonsandtrolls_effect_instance = DungeonsandtrollsEffect.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsEffect.to_json()

# convert the object into a dict
dungeonsandtrolls_effect_dict = dungeonsandtrolls_effect_instance.to_dict()
# create an instance of DungeonsandtrollsEffect from a dict
dungeonsandtrolls_effect_form_dict = dungeonsandtrolls_effect.from_dict(dungeonsandtrolls_effect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


