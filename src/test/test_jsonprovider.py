import pytest

from src.model.jsonprovider import ChampionJsonProvider
from src.model.jsonprovider import InvalidPatchOrRegionError


PATCH: str = '9.3.1'
REGION: str = 'ja_JP'


def test_happypath():
    json_provider = ChampionJsonProvider()
    champion_json = json_provider.provide(PATCH, REGION)
    with open('{0}.json'.format(PATCH)) as patch_json:
        assert champion_json == patch_json.read()


def test_invalid_patch():
    with pytest.raises(InvalidPatchOrRegionError):
        ChampionJsonProvider().provide('0.0.0', REGION)


def test_invalid_region():
    with pytest.raises(InvalidPatchOrRegionError):
        ChampionJsonProvider().provide(PATCH, 'NA>EU')
