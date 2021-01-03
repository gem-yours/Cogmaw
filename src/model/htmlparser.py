from typing import List
from functools import reduce
from bs4 import BeautifulSoup

from src.entity.champion import Champion


def search_by_attr(attr: str, value: str):
    return lambda tag: tag.has_attr(attr) and tag[attr] == value


def search_by_id(element_id: str):
    return search_by_attr('id', element_id)


def search_by_data_source(data_source: str):
    return search_by_attr('data-source', data_source)


def tag_name_and_per_level_tag_name(tag_name: str) -> List[str]:
    return [tag_name, tag_name + '_lvl']


def optional_float(value: str) -> float:
    if value is None:
        return 0
    return float(value)


class ChampionHTMLParser:
    """
    parse html from https://leagueoflegends.fandom.com/wiki/List_of_champions
    """
    champion_name: str = ''
    soup: BeautifulSoup

    def __init__(self, champion_name):
        self.champion_name = champion_name
        # TODO: download html from wiki
        self.soup = BeautifulSoup(
            open('html/{0} _ League of Legends Wiki _ Fandom.html'.format(self.champion_name)),
            'html5lib'
        )

    def parse(self) -> Champion:
        champion = Champion()
        status = self.__get_status()
        champion.health = status[0]
        champion.health_growth = status[1]
        champion.health_regen = status[2]
        champion.attack_damage = status[3]
        champion.attack_damage_growth = status[4]
        champion.armor = status[5]
        champion.armor_growth = status[6]
        champion.magic_resist = status[7]
        champion.magic_resist_growth = status[8]
        champion.resource_name = self.__get_resource_name()
        optional_status = self.__get_optional_status()
        champion.resource = optional_status[0]
        champion.resource_growth = optional_status[1]
        champion.resource_regen = optional_status[2]
        champion.resource_regen_growth = optional_status[3]

        champion.resource_name = self.__get_resource_name()

        return champion

    """
    get parameters from html (exclude resources, resource regen and attack speed)
    """

    def __get_status(self) -> List[float]:
        return [float(self.soup.find(search_by_id(element_id)).text) for element_id in self.__status_name()]

    """
    get all status id (include per level)
    """

    def __status_name(self) -> List[str]:
        scaled_status = [
            'Health_{0}',
            'HealthRegen_{0}',
            'AttackDamage_{0}',
            'Armor_{0}',
            'MagicResist_{0}',
        ]
        static_status = [
            'AttackRange_{0}',
            'MovementSpeed_{0}'
        ]
        scaled_ids = [tag_name_and_per_level_tag_name(tag_name) for tag_name in scaled_status]
        scaled_ids = reduce(lambda a, b: a + b, scaled_ids)
        return [tag_name.format(self.champion_name) for tag_name in scaled_ids + static_status]

    def __get_optional_status(self) -> List[float]:
        return [optional_float(self.soup.find(search_by_id(resource)).text) for resource in self.__get_optional_status_name()]

    def __get_optional_status_name(self) -> List[str]:
        status = [
            'ResourceBar_{0}',
            'ResourceRegen_{0}'
        ]
        scaled_status = [tag_name_and_per_level_tag_name(tag_name) for tag_name in status]
        flatten_status = reduce(lambda a, b: a + b, scaled_status)
        return [status_name.format(self.champion_name) for status_name in flatten_status]

    def __get_resource_name(self) -> str:
        resource_name = self.soup.find(search_by_data_source('resource')).text
        resource_name = resource_name.replace('\n', '') \
            .replace('\t', '') \
            .replace('Resource ', '') \
            .replace('Energy', '気') \
            .replace('Manaless ( Blood Well)', 'ブラッドウェル') \
            .replace('Rage', 'ぷんすこ') \
            .replace('Ferocity', 'フェロシティ') \
            .replace('Fury', 'フューリー') \
            .replace('Bloodthirst', '狂喜') \
            .replace('Grid', '闘魂') \
            .replace('Heat', 'ヒート')\
            .replace('Mana', 'マナ')
        return resource_name
