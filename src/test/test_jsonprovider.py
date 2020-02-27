import pytest

from src.model.jsonprovider import ChampionJsonProvider
from src.model.jsonprovider import InvalidPatchError


def test_happypath_with_nocache():
    json_provider = ChampionJsonProvider()
    champion_json = json_provider.provide('9.3.1')
    with open('9.3.1.json') as patch_json:
        assert champion_json == patch_json.read()


def test_invalid_patch():
    with pytest.raises(InvalidPatchError):
        ChampionJsonProvider().provide('0.0.0')
