# DungeonsandtrollsSkillFlags


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requires_alone** | **bool** |  | [optional] 
**requires_line_of_sight** | **bool** |  | [optional] 
**allow_target_self** | **bool** |  | [optional] 
**movement** | **bool** |  | [optional] 
**knockback** | **bool** |  | [optional] 
**stun** | **bool** |  | [optional] 
**ground_effect** | **bool** |  | [optional] 
**passive** | **bool** |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_skill_flags import DungeonsandtrollsSkillFlags

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsSkillFlags from a JSON string
dungeonsandtrolls_skill_flags_instance = DungeonsandtrollsSkillFlags.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsSkillFlags.to_json()

# convert the object into a dict
dungeonsandtrolls_skill_flags_dict = dungeonsandtrolls_skill_flags_instance.to_dict()
# create an instance of DungeonsandtrollsSkillFlags from a dict
dungeonsandtrolls_skill_flags_form_dict = dungeonsandtrolls_skill_flags.from_dict(dungeonsandtrolls_skill_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


