## Description
Download and parse LoL champions json from (ddragon) [http://ddragon.leagueoflegends.com/cdn/].

## usage
``` sample.py
from typing import List

from src.model.jsonprovider import ChampionJsonProvider
from src.entity.champion import Champion
import src.model.parser as parser

# download champion status in patch 9.2.1.
json = ChampionJsonProvider().provide('9.2.1')
# parse it
champions: List[Champion] = parser.parse(json)
# output is 'Aatrox'
print(champions[0].name)

```