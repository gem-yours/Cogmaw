from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import re

from src.model.parser import parse
from src.model.sender import ChampionDataSender
from src.model.jsonprovider import ChampionJsonProvider

with open('test/Aatrox.json') as file:
    json = file.read()

json_provider = ChampionJsonProvider()
json = json_provider.provide("10.2.1", "ja_JP")

champions = parse(json)

sender = ChampionDataSender('http://0.0.0.0:8000/velkoz/')

[sender.send(champion) for champion in champions]