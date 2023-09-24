# coding: utf-8

"""
    Dungeons and Trolls

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from dungeons_and_trolls_client.models.dungeonsandtrolls_map import DungeonsandtrollsMap  # noqa: E501

class TestDungeonsandtrollsMap(unittest.TestCase):
    """DungeonsandtrollsMap unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DungeonsandtrollsMap:
        """Test DungeonsandtrollsMap
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DungeonsandtrollsMap`
        """
        model = DungeonsandtrollsMap()  # noqa: E501
        if include_optional:
            return DungeonsandtrollsMap(
                levels = [
                    dungeons_and_trolls_client.models.dungeonsandtrolls_level.dungeonsandtrollsLevel(
                        level = 56, 
                        width = 56, 
                        height = 56, 
                        free = [
                            [
                                None
                                ]
                            ], 
                        objects = [
                            dungeons_and_trolls_client.models.dungeonsandtrolls_map_objects.dungeonsandtrollsMapObjects(
                                position = dungeons_and_trolls_client.models.dungeonsandtrolls_position.dungeonsandtrollsPosition(
                                    position_x = 56, 
                                    position_y = 56, ), 
                                monsters = [
                                    dungeons_and_trolls_client.models.dungeonsandtrolls_monster.dungeonsandtrollsMonster(
                                        id = '', 
                                        name = '', 
                                        icon = '', 
                                        items = [
                                            dungeons_and_trolls_client.models.dungeonsandtrolls_simple_item.dungeonsandtrollsSimpleItem(
                                                name = '', 
                                                slot = 'head', 
                                                icon = '', )
                                            ], 
                                        effects = [
                                            dungeons_and_trolls_client.models.dungeonsandtrolls_effect.dungeonsandtrollsEffect(
                                                damage_amount = 1.337, 
                                                damage_type = 'slash', 
                                                duration = 56, 
                                                caster_id = '', )
                                            ], 
                                        life_percentage = 1.337, 
                                        faction = '', 
                                        attributes = dungeons_and_trolls_client.models.dungeonsandtrolls_attributes.dungeonsandtrollsAttributes(
                                            strength = 1.337, 
                                            dexterity = 1.337, 
                                            intelligence = 1.337, 
                                            willpower = 1.337, 
                                            constitution = 1.337, 
                                            slash_resist = 1.337, 
                                            pierce_resist = 1.337, 
                                            fire_resist = 1.337, 
                                            poison_resist = 1.337, 
                                            electric_resist = 1.337, 
                                            life = 1.337, 
                                            stamina = 1.337, 
                                            mana = 1.337, 
                                            constant = 1.337, ), 
                                        equipped_items = [
                                            dungeons_and_trolls_client.models.dungeonsandtrolls_item.dungeonsandtrollsItem(
                                                id = '', 
                                                name = '', 
                                                price = 56, 
                                                requirements = dungeons_and_trolls_client.models.dungeonsandtrolls_attributes.dungeonsandtrollsAttributes(
                                                    strength = 1.337, 
                                                    dexterity = 1.337, 
                                                    intelligence = 1.337, 
                                                    willpower = 1.337, 
                                                    constitution = 1.337, 
                                                    slash_resist = 1.337, 
                                                    pierce_resist = 1.337, 
                                                    fire_resist = 1.337, 
                                                    poison_resist = 1.337, 
                                                    electric_resist = 1.337, 
                                                    life = 1.337, 
                                                    stamina = 1.337, 
                                                    mana = 1.337, 
                                                    constant = 1.337, ), 
                                                skills = [
                                                    dungeons_and_trolls_client.models.dungeonsandtrolls_skill.dungeonsandtrollsSkill(
                                                        id = '', 
                                                        name = '', 
                                                        target = 'none', 
                                                        cost = , 
                                                        range = , 
                                                        radius = , 
                                                        duration = , 
                                                        damage_amount = , 
                                                        caster_effects = dungeons_and_trolls_client.models.dungeonsandtrolls_skill_effect.dungeonsandtrollsSkillEffect(
                                                            flags = dungeons_and_trolls_client.models.dungeonsandtrolls_skill_flags.dungeonsandtrollsSkillFlags(
                                                                requires_alone = True, 
                                                                requires_line_of_sight = True, 
                                                                allow_target_self = True, 
                                                                movement = True, 
                                                                knockback = True, 
                                                                stun = True, 
                                                                ground_effect = True, 
                                                                passive = True, ), 
                                                            summons = [
                                                                dungeons_and_trolls_client.models.dungeonsandtrolls_droppable.dungeonsandtrollsDroppable(
                                                                    skill = dungeons_and_trolls_client.models.dungeonsandtrolls_skill.dungeonsandtrollsSkill(
                                                                        id = '', 
                                                                        name = '', 
                                                                        target_effects = dungeons_and_trolls_client.models.dungeonsandtrolls_skill_effect.dungeonsandtrollsSkillEffect(), ), 
                                                                    item = dungeons_and_trolls_client.models.dungeonsandtrolls_item.dungeonsandtrollsItem(
                                                                        id = '', 
                                                                        name = '', 
                                                                        price = 56, 
                                                                        icon = '', 
                                                                        unidentified = True, ), 
                                                                    monster = dungeons_and_trolls_client.models.dungeonsandtrolls_monster.dungeonsandtrollsMonster(
                                                                        id = '', 
                                                                        name = '', 
                                                                        icon = '', 
                                                                        life_percentage = 1.337, 
                                                                        faction = '', 
                                                                        score = 1.337, 
                                                                        algorithm = '', 
                                                                        on_death = [
                                                                            dungeons_and_trolls_client.models.dungeonsandtrolls_droppable.dungeonsandtrollsDroppable(
                                                                                decoration = dungeons_and_trolls_client.models.dungeonsandtrolls_decoration.dungeonsandtrollsDecoration(
                                                                                    name = '', 
                                                                                    type = '', 
                                                                                    icon = '', ), 
                                                                                waypoint = dungeons_and_trolls_client.models.dungeonsandtrolls_waypoint.dungeonsandtrollsWaypoint(
                                                                                    destination_floor = 56, ), 
                                                                                key = dungeons_and_trolls_client.models.dungeonsandtrolls_key.dungeonsandtrollsKey(
                                                                                    doors = [
                                                                                        dungeons_and_trolls_client.models.dungeonsandtrolls_position.dungeonsandtrollsPosition(
                                                                                            position_x = 56, 
                                                                                            position_y = 56, )
                                                                                        ], ), )
                                                                            ], ), 
                                                                    decoration = dungeons_and_trolls_client.models.dungeonsandtrolls_decoration.dungeonsandtrollsDecoration(
                                                                        name = '', 
                                                                        type = '', 
                                                                        icon = '', ), 
                                                                    waypoint = dungeons_and_trolls_client.models.dungeonsandtrolls_waypoint.dungeonsandtrollsWaypoint(
                                                                        destination_floor = 56, ), 
                                                                    key = dungeons_and_trolls_client.models.dungeonsandtrolls_key.dungeonsandtrollsKey(), )
                                                                ], ), 
                                                        target_effects = , )
                                                    ], 
                                                icon = '', 
                                                unidentified = True, )
                                            ], 
                                        score = 1.337, 
                                        algorithm = '', 
                                        on_death = [
                                            
                                            ], )
                                    ], 
                                players = [
                                    dungeons_and_trolls_client.models.dungeonsandtrolls_character.dungeonsandtrollsCharacter(
                                        id = '', 
                                        name = '', 
                                        money = 56, 
                                        equip = [
                                            
                                            ], 
                                        score = 1.337, 
                                        skill_points = 1.337, )
                                    ], 
                                is_stairs = True, 
                                portal = , 
                                decorations = [
                                    
                                    ], 
                                effects = [
                                    dungeons_and_trolls_client.models.dungeonsandtrolls_effect.dungeonsandtrollsEffect(
                                        caster_id = '', )
                                    ], 
                                items = [
                                    
                                    ], 
                                is_free = True, 
                                is_wall = True, 
                                is_door = True, 
                                is_spawn = True, )
                            ], 
                        ascii = [
                            ''
                            ], )
                    ]
            )
        else:
            return DungeonsandtrollsMap(
        )
        """

    def testDungeonsandtrollsMap(self):
        """Test DungeonsandtrollsMap"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
