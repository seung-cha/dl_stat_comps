from abc import ABC, abstractmethod

class Weapon:
    def __init__(   self,\
                    base_bullet_damage:     float   = .0,\
                    shots_per_second:       float   = .0,\
                    ammo:                   int     = 0,\
                    reload_time:            float   = .0,\
                    light_melee_damage:     float   = .0,\
                    heavy_melee_damage:     float   = .0,):
        self.base_bullet_damage             = base_bullet_damage
        self.shots_per_second               = shots_per_second
        self.ammo                           = ammo
        self.reload_time                    = reload_time
        self.light_melee_damage             = light_melee_damage
        self.heavy_melee_damage             = heavy_melee_damage


class Vitality:
    def __init__(   self,\
                    max_health:             float   = .0,\
                    health_regen:           float   = .0,\
                    crit_reduction:         float   = .0,\
                    move_speed:             float   = .0,\
                    sprint_speed:           float   = .0,\
                    stamina_cooldown:       float   = .0,\
                    stamina_count:          int     =  0,):
        self.max_health                     = max_health
        self.health_regen                   = health_regen
        self.crit_reduction                 = crit_reduction
        self.move_speed                     = move_speed
        self.sprint_speed                   = sprint_speed
        self.stamina_cooldown               = stamina_cooldown
        self.stamina_count                  = stamina_count

class Spirit:
    def __init__(   self,\
                    spirit_power:           int     = 0):
        self.spirit_power = spirit_power


class Growth:
    def __init__(   self,
                    bullet_damage:          float   = 0.,\
                    light_melee_damage:     float   = 0.,\
                    max_health:             float   = 0.,\
                    spirit_power:           float   = 0.):
        self.bullet_damage                  = bullet_damage
        self.light_melee_damage             = light_melee_damage
        self.max_health                     = max_health
        self.spirit_power                   = spirit_power



class Character:
    def __init__(self):
        self.weapon     = Weapon()
        self.vitality   = Vitality()
        self.spirit     = Spirit()
        self.growth     = Growth()