from os.path import exists
from http.client import HTTPResponse
from urllib import request
from urllib.error import HTTPError


class InvalidPatchOrRegionError(Exception):
    def __init__(self, patch: str, region: str):
        """
        This exception caused by wrong patch format string.
        :param patch: patch string e.g. '9.2.4'
        :param patch: region string e.g ja_JP
        """
        self.message = "patch {0} region {1} is invalid format".format(patch, region)


class ChampionJsonProvider:
    """
    This class provides Champion json.
    Download it if needed.
    """
    JSON_PATH: str = 'json/{0}'
    D_DRAGON_URL: str = 'http://ddragon.leagueoflegends.com/cdn/{0}/data/{1}/champion.json'

    recently_accessed_patch: str
    champions_json: str  # cache the most recently accessed

    def __download_json(self, patch: str, region: str) -> str:
        """
        download champion json from d-dragon and save it as file
        :param patch: patch string e.g. '9.2.4'
        :return:
        """
        req = request.Request(self.D_DRAGON_URL.format(patch, region))
        try:
            res: HTTPResponse = request.urlopen(req)
        except HTTPError:
            raise InvalidPatchOrRegionError(patch, region)
        with res:
            body = res.read()
        return body.decode()

    def provide(self, patch: str, region: str) -> str:
        """
        return json str that has champion information
        :param patch patch string e.g. '9.2.4'
        :param region region name e.g. ja_JP
        """
        file_path = self.JSON_PATH.format(region + patch + '.json')
        if exists(file_path):
            with open(file_path) as file:
                return file.read()
        else:
            json = self.__download_json(patch, region)
            with open(file_path, 'w+') as file:
                file.write(json)
            return json
