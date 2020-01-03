import json

from src.entity.champion import Champion


def parse(json_str: str) -> Champion:
    """
    parse json that has champion information
    :param json_str: json
    :return: Champion object
    """
    champion_json = json.loads(json_str)
    champion = Champion()
    champion.patch = champion_json['version']
    champion.name = next(iter(champion_json['data']))
    champion.japanese_name = champion_json['data'][champion.name]['name']
    champion.resource_name = champion_json['data'][champion.name]['partype']

    stats = champion_json['data'][champion.name]['stats']

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
