from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import re

from src.model.parser import parse
from src.model.sender import ChampionDataSender
from src.model.jsonprovider import ChampionJsonProvider
import requests
import base64

# res = requests.get('http://ddragon.leagueoflegends.com/cdn/11.12.1/img/champion/Aatrox.png')
# encoded_string = base64.b64encode(res.content)
# print(encoded_string.decode('utf-8'))


with open('test/Aatrox.json') as file:
    json = file.read()

json_provider = ChampionJsonProvider()
json = json_provider.provide("10.25.1", "ja_JP")

champions = parse(json)

sender = ChampionDataSender('http://0.0.0.0:8000/velkoz/')

# [sender.send(champion) for champion in champions]
sender.send(champions[0])

# import json
# import os
# import django
# from django.core.files.uploadedfile import SimpleUploadedFile
# django.setup()
# from graphene_file_upload.django.testing import file_graphql_query
#
# def client_query(client):
#     def func(*args, **kwargs):
#         return file_graphql_query(*args, **kwargs, client=client)
#
#     return func
#

# # Test your query using the client_query fixture
# def test_some_query(file_content):
#     test_file = SimpleUploadedFile(name='test.txt', content=file_content.encode('utf-8'))
#
#     response = client_query(
#         '''
#         mutation testMutation($file: Upload!) {
#             myUpload(fileIn: $file) {
#                 ok
#             }
#         }
#         ''',
#         op_name='testMutation',
#         files={'file': test_file}
#     )
#
#     content = json.loads(response.content)
#     print(content)
#
# test_some_query("test")
