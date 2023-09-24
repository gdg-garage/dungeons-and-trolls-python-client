# DungeonsandtrollsSkillEffect


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**DungeonsandtrollsSkillAttributes**](DungeonsandtrollsSkillAttributes.md) |  | [optional] 
**flags** | [**DungeonsandtrollsSkillFlags**](DungeonsandtrollsSkillFlags.md) |  | [optional] 
**summons** | [**List[DungeonsandtrollsDroppable]**](DungeonsandtrollsDroppable.md) |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_skill_effect import DungeonsandtrollsSkillEffect

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsSkillEffect from a JSON string
dungeonsandtrolls_skill_effect_instance = DungeonsandtrollsSkillEffect.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsSkillEffect.to_json()

# convert the object into a dict
dungeonsandtrolls_skill_effect_dict = dungeonsandtrolls_skill_effect_instance.to_dict()
# create an instance of DungeonsandtrollsSkillEffect from a dict
dungeonsandtrolls_skill_effect_form_dict = dungeonsandtrolls_skill_effect.from_dict(dungeonsandtrolls_skill_effect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


