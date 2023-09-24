# DungeonsandtrollsAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strength** | **float** |  | [optional] 
**dexterity** | **float** |  | [optional] 
**intelligence** | **float** |  | [optional] 
**willpower** | **float** |  | [optional] 
**constitution** | **float** |  | [optional] 
**slash_resist** | **float** |  | [optional] 
**pierce_resist** | **float** |  | [optional] 
**fire_resist** | **float** |  | [optional] 
**poison_resist** | **float** |  | [optional] 
**electric_resist** | **float** |  | [optional] 
**life** | **float** |  | [optional] 
**stamina** | **float** |  | [optional] 
**mana** | **float** |  | [optional] 
**constant** | **float** |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_attributes import DungeonsandtrollsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsAttributes from a JSON string
dungeonsandtrolls_attributes_instance = DungeonsandtrollsAttributes.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsAttributes.to_json()

# convert the object into a dict
dungeonsandtrolls_attributes_dict = dungeonsandtrolls_attributes_instance.to_dict()
# create an instance of DungeonsandtrollsAttributes from a dict
dungeonsandtrolls_attributes_form_dict = dungeonsandtrolls_attributes.from_dict(dungeonsandtrolls_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


