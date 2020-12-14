import pytest
from json import JSONDecodeError

from src.entity.champion import Champion
import src.model.parser as parser


def create_champion() -> Champion:
    """
    create correct aatrox information
    :return aatrox champion object
    """
    aatrox: Champion = Champion()
    aatrox.patch = "9.5.1"
    # correct_aatrox.image  # not implemented now
    aatrox.name = "Aatrox"
    aatrox.japanese_name = "エイトロックス"
    aatrox.health = 580
    aatrox.health_growth = 80
    aatrox.health_regen = 8
    aatrox.health_regen_growth = 0.75
    aatrox.resource_name = "ブラッドウェル"
    aatrox.resource = 0
    aatrox.resource_growth = 0
    aatrox.resource_regen = 0
    aatrox.resource_regen_growth = 0
    aatrox.attack_damage = 60
    aatrox.attack_damage_growth = 5
    aatrox.attack_speed = 0.651
    aatrox.attack_speed_growth = 2.5
    aatrox.range = 175
    aatrox.armor = 33
    aatrox.armor_growth = 3.25
    aatrox.magic_resist = 32.1
    aatrox.magic_resist_growth = 1.25
    aatrox.move_speed = 345

    return aatrox


def parse_champion() -> Champion:
    """
    create aatrox information from json file
    :return: aatrox champion object
    """{
  "version": "9.5.1",
  "data": {
    "Aatrox": {
      "id": "Aatrox",
      "name": "エイトロックス",
      "image": {
        "full": "Aatrox.png",
        "sprite": "champion0.png",
        "group": "champion",
        "x": 0,
        "y": 0,
        "w": 48,
        "h": 48
      },
      "stats": {
        "hp": 580,
        "hpperlevel": 80,
        "mp": 0,
        "mpperlevel": 0,
        "movespeed": 345,
        "armor": 33,
        "armorperlevel": 3.25,
        "spellblock": 32.1,
        "spellblockperlevel": 1.25,
        "attackrange": 175,
        "hpregen": 8,
        "hpregenperlevel": 0.75,
        "mpregen": 0,
        "mpregenperlevel": 0,
        "crit": 0,
        "critperlevel": 0,
        "attackdamage": 60,
        "attackdamageperlevel": 5,
        "attackspeedperlevel": 2.5,
        "attackspeed": 0.651
      },
      "partype": "ブラッドウェル"
    }
  }
}
    with open('Aatrox.json') as file:
        json = file.read()
    return parser.parse(json)


def test_happypath():
    assert create_champion() == parse_champion()[0]


def test_invalid_format():
    with pytest.raises(JSONDecodeError):
        parser.parse('invalid format')


def test_empty_str():
    with pytest.raises(JSONDecodeError):
        parser.parse('')


