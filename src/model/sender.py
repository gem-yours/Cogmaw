from urllib import request
from urllib.error import HTTPError

from src.entity.champion import Champion


class InvalidChampion(Exception):
    def __init__(self, parameter_name: str, parameter: str):
        self.message = "Champion parameter {0}={1} is wrong.".format(parameter_name, parameter)


class ChampionDataSender():
    """
    send Champion data to graphql server
    """
    __SERVER_URL = '0.0.0.0:8000/velkoz'

    def send(self, champion: Champion):
        if champion == None:
            raise InvalidChampion("champion", "None")

        req = request.Request(self.__SERVER_URL)
        req.method = 'POST'
        pass
