# DungeonsandtrollsSkill


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**target** | [**SkillTarget**](SkillTarget.md) |  | [optional] 
**cost** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**range** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**radius** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**duration** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**damage_amount** | [**DungeonsandtrollsAttributes**](DungeonsandtrollsAttributes.md) |  | [optional] 
**damage_type** | [**DungeonsandtrollsDamageType**](DungeonsandtrollsDamageType.md) |  | [optional] 
**caster_effects** | [**DungeonsandtrollsSkillEffect**](DungeonsandtrollsSkillEffect.md) |  | [optional] 
**target_effects** | [**DungeonsandtrollsSkillEffect**](DungeonsandtrollsSkillEffect.md) |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_skill import DungeonsandtrollsSkill

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsSkill from a JSON string
dungeonsandtrolls_skill_instance = DungeonsandtrollsSkill.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsSkill.to_json()

# convert the object into a dict
dungeonsandtrolls_skill_dict = dungeonsandtrolls_skill_instance.to_dict()
# create an instance of DungeonsandtrollsSkill from a dict
dungeonsandtrolls_skill_form_dict = dungeonsandtrolls_skill.from_dict(dungeonsandtrolls_skill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


