
class Champion(object):
    image: str  # not implemented now. should create ChampionImage class
    name: str  # English name
    japanese_name: str

    health: float
    health_growth: float
    health_regen: float
    health_regen_growth: float

    resource_name: str
    resource: float
    resource_growth: float
    resource_regen: float
    resource_regen_growth: float

    range: float

    attack_damage: float
    attack_damage_growth: float

    attack_speed: float
    attack_speed_growth: float

    armor: float
    armor_growth: float

    magic_resist: float
    magic_resist_growth: float

    move_speed: float

    def __eq__(self, other):
        return vars(self) == vars(other)



