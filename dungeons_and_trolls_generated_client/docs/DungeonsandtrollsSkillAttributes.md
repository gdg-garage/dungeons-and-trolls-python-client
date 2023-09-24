# DungeonsandtrollsSkillAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strength** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**dexterity** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**intelligence** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**willpower** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**constitution** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**slash_resist** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**pierce_resist** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**fire_resist** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**poison_resist** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**electric_resist** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**life** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**stamina** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**mana** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**constant** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_skill_attributes import DungeonsandtrollsSkillAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsSkillAttributes from a JSON string
dungeonsandtrolls_skill_attributes_instance = DungeonsandtrollsSkillAttributes.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsSkillAttributes.to_json()

# convert the object into a dict
dungeonsandtrolls_skill_attributes_dict = dungeonsandtrolls_skill_attributes_instance.to_dict()
# create an instance of DungeonsandtrollsSkillAttributes from a dict
dungeonsandtrolls_skill_attributes_form_dict = dungeonsandtrolls_skill_attributes.from_dict(dungeonsandtrolls_skill_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


