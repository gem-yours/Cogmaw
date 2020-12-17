from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

from src.entity.champion import Champion


class InvalidChampion(Exception):
    def __init__(self, parameter_name: str, parameter: str):
        self.message = "Champion parameter {0}={1} is wrong.".format(parameter_name, parameter)


class ChampionDataSender:
    """
    send Champion data to graphql server
    """

    def __init__(self, base_url: str):
        self.base_url = base_url

    base_url: str
    __MUTATION_TEMPLATE = '''
        mutation createChamp {{
          createChampion(championData: {{
            name: "{0}"
            japaneseName: "{1}"
            patch: "{2}"
            health: {3}
            healthGrowth: {4}
            healthRegen: {5}
            healthRegenGrowth: {6}
            resourceName: "{7}"
            resource: {8}
            resourceGrowth: {9}
            resourceRegen: {10}
            resourceRegenGrowth: {11}
            attackDamage: {12}
            attackDamageGrowth: {13}
            attackSpeed: {14}
            attackSpeedGrowth: {15}
            armor: {16}
            armorGrowth: {17}
            magicResist: {18}
            magicResistGrowth: {19}
            moveSpeed: {20}
          }}) {{
            champion {{
              name
            }}
          }}
        }}
    '''

    def send(self, champion: Champion):
        if champion is None:
            raise InvalidChampion("champion", "None")

        transport = RequestsHTTPTransport(
            url=self.base_url,
            use_json=True,
            headers={
                "Content-type": "application/json",
            },
            retries=3,
            verify=False
        )
        client = Client(
            transport=transport,
            fetch_schema_from_transport=True,
        )
        # TODO: テンプレートにパラメータを入れてgqlで送信する
        query_str: str = self.__MUTATION_TEMPLATE.format(
            champion.name,
            champion.japanese_name,
            champion.patch,
            champion.health,
            champion.health_growth,
            champion.health_regen,
            champion.health_regen_growth,
            champion.resource_name,
            champion.resource,
            champion.resource_growth,
            champion.resource_regen,
            champion.resource_regen_growth,
            champion.attack_damage,
            champion.attack_damage_growth,
            champion.attack_speed,
            champion.attack_speed_growth,
            champion.armor,
            champion.armor_growth,
            champion.magic_resist,
            champion.magic_resist_growth,
            champion.move_speed
        )
        query = gql(query_str)
        client.execute(query)
