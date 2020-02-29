import json
from typing import List

from src.entity.champion import Champion


def parse(json_str: str) -> List[Champion]:
    """
    parse json that has champion information
    :param json_str: json
    :return: Champion object
    """
    champion_json = json.loads(json_str)

    return  [__convert_dict_to_champion(champion_json['data'][champion_name], champion_name, champion_json['version']) \
             for champion_name in \
             iter(champion_json['data'])]


def __convert_dict_to_champion(champion_data: dict, champion_name: str, patch: str):
    champion = Champion()
    champion.patch = patch
    champion.name = champion_name
    champion.japanese_name = champion_data['name']
    champion.resource_name = champion_data['partype']

    stats = champion_data['stats']

    champion.health = stats['hp']
    champion.health_growth = stats['hpperlevel']
    champion.health_regen = stats['hpregen']
    champion.health_regen_growth = stats['hpregenperlevel']

    champion.resource_name
    champion.resource = stats['mp']
    champion.resource_growth = stats['mpperlevel']
    champion.resource_regen = stats['mpregen']
    champion.resource_regen_growth = stats['mpregenperlevel']

    champion.range = stats['attackrange']

    champion.attack_damage = stats['attackdamage']
    champion.attack_damage_growth = stats['attackdamageperlevel']

    champion.attack_speed = stats['attackspeed']
    champion.attack_speed_growth = stats['attackspeedperlevel']

    champion.armor = stats['armor']
    champion.armor_growth = stats['armorperlevel']

    champion.magic_resist = stats['spellblock']
    champion.magic_resist_growth = stats['spellblockperlevel']

    champion.move_speed = stats['movespeed']

    return champion
