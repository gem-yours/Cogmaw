from os.path import exists
import requests
import base64


class InvalidPatchOrRegionError(Exception):
    def __init__(self, patch: str, champion_name: str):
        """
        This exception caused by wrong patch format string.
        :param patch: patch string e.g. '9.2.4'
        :param patch: region string e.g ja_JP
        """
        self.message = "patch {0} champion {1} is invalid format".format(patch, champion_name)

class IconProvider:
    """
    This class provides Champion Icon
    """
    IMAGE_PATH = 'icon/{0}'
    D_DRAGON_URL = 'http://ddragon.leagueoflegends.com/cdn/{0}/img/champion/{1}.png'

    def __download_icon(self, patch: str, champion_name: str) -> bytes:
        """
        download champion icon from d-dragon
        :param patch: e.g. '9.2.4'
        :param champion_name: e.g. 'Aatrox'
        :return: champion image byte date
        """
        try:
            res = requests.get(self.D_DRAGON_URL.format(patch, champion_name))
            res.raise_for_status()
        except requests.exceptions.HTTPError:
            raise InvalidPatchOrRegionError(patch, champion_name)
        with res:
            return res.content

    def provide(self, patch: str, champion_name: str) -> bytes:
        """
        return champion image from ddragon or cache
        :param patch: e.g. '9.2.4'
        :param champion_name: e.g. 'Aatrox'
        :return:
        """
        file_path = self.IMAGE_PATH.format(champion_name + patch + '.png')
        if exists(file_path):
            with open(file_path, 'rb') as file:
                return file.read()
        else:
            image = self.__download_icon(patch, champion_name)
            with open(file_path, 'wb+') as file:
                file.write(image)
            return image

    def provide_base64(self, patch: str, champion_name: str) -> str:
        """
        return champion image as base64 from ddragon or cache
        :param patch: e.g. '9.2.4'
        :param champion_name: e.g. 'Aatrox'
        :return:
        """
        return base64.b64encode(self.provide(patch, champion_name)).decode('utf-8')
