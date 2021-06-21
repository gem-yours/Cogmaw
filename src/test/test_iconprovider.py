import pytest
import base64

from src.model.iconprovider import IconProvider
from src.model.iconprovider import InvalidPatchOrRegionError


PATCH: str = '9.3.1'
CHAMPION_NAME: str = 'Aatrox'


def test_provide():
    icon_provider = IconProvider()
    icon = icon_provider.provide(PATCH, CHAMPION_NAME)
    with open('{0}.png'.format(CHAMPION_NAME), 'rb') as patch_json:
        assert icon == patch_json.read()

def test_base64():
    icon_provider = IconProvider()
    icon = icon_provider.provide_base64(PATCH, CHAMPION_NAME)
    with open('{0}.png'.format(CHAMPION_NAME), 'rb') as patch_json:
        assert icon == base64.b64encode(patch_json.read()).decode('utf-8')



def test_invalid_patch():
    with pytest.raises(InvalidPatchOrRegionError):
        IconProvider().provide('0.0.0', CHAMPION_NAME)


def test_invalid_region():
    with pytest.raises(InvalidPatchOrRegionError):
        IconProvider().provide(PATCH, 'Ao Shin')
