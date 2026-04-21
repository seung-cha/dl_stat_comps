from . import stats_base as stats

class HeroUnit:
    def __init__(self, name: str, icon: str, stats= stats.Character()):
        self.stats = stats
        self.name = name
        self.icon = icon

    def __str__(self):
        return f"![{self.name}]({self.icon}) {self.name}"

def get_dummy() -> HeroUnit:
    return HeroUnit(name= "Dummy", icon= "")

def get_abrams() -> HeroUnit:
    return HeroUnit(name= 'Abrams', icon= "https://assets-bucket.deadlock-api.com/assets-api-res/images/heroes/bull_card.webp",\
                    stats= stats.Character(
                        weapon= stats.Weapon(
                            base_bullet_damage=     3.6,    \
                            ammo=                   9,      \
                            shots_per_second=       1.59,   \
                            reload_time=            0.35,   \
                            light_melee_damage=     50,     \
                            heavy_melee_damage=     92,),
                        vitality= stats.Vitality(
                            max_health=             810,    \
                            health_regen=           1.5,    \
                            move_speed=             6.4,    \
                            sprint_speed=           1.6,    \
                            stamina_cooldown=       4.5,    \
                            stamina_count=          3,),
                        growth= stats.Growth(
                            bullet_damage=          0.1,    \
                            light_melee_damage=     1.74,   \
                            max_health=             62,     \
                            spirit_power=           1.1,)))