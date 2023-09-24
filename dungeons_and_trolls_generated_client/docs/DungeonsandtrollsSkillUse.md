# DungeonsandtrollsSkillUse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skill_id** | **str** |  | [optional] 
**target_id** | **str** |  | [optional] 
**position** | [**DungeonsandtrollsPosition**](DungeonsandtrollsPosition.md) |  | [optional] 

## Example

```python
from dungeons_and_trolls_client.models.dungeonsandtrolls_skill_use import DungeonsandtrollsSkillUse

# TODO update the JSON string below
json = "{}"
# create an instance of DungeonsandtrollsSkillUse from a JSON string
dungeonsandtrolls_skill_use_instance = DungeonsandtrollsSkillUse.from_json(json)
# print the JSON string representation of the object
print DungeonsandtrollsSkillUse.to_json()

# convert the object into a dict
dungeonsandtrolls_skill_use_dict = dungeonsandtrolls_skill_use_instance.to_dict()
# create an instance of DungeonsandtrollsSkillUse from a dict
dungeonsandtrolls_skill_use_form_dict = dungeonsandtrolls_skill_use.from_dict(dungeonsandtrolls_skill_use_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


