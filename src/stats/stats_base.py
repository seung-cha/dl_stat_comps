from abc import ABC, abstractmethod
import streamlit as st

class Weapon:
    def __init__(   self,\
                    base_bullet_damage:         float   = .0,\
                    bonus_bullet_damage:        float   = .0,\
                    shots_per_second:           float   = .0,\
                    bonus_fire_rate:            float   = .0,\
                    bullet_speed:               float   = .0,\
                    bonus_bullet_speed:         float   = .0,\
                    ammo:                       int     =  0,\
                    bonus_ammo_perc:            float   = .0,\
                    bonus_ammo:                 int     =  0,\
                    reload_time:                float   = .0,\
                    light_melee_damage:         float   = .0,\
                    heavy_melee_damage:         float   = .0,\
                    bonus_melee_damage:         float   = .0,\
                    bonus_heavy_melee_damage:   float = .0,):
        self.base_bullet_damage             = base_bullet_damage
        self.bonus_bullet_damage            = bonus_bullet_damage
        self.shots_per_second               = shots_per_second
        self.bonus_fire_rate                = bonus_fire_rate
        self.bullet_speed                   = bullet_speed
        self.bonus_bullet_speed             = bonus_bullet_speed
        self.ammo                           = ammo
        self.bonus_ammo_perc                = bonus_ammo_perc
        self.bonus_ammo                     = bonus_ammo
        self.reload_time                    = reload_time
        self.light_melee_damage             = light_melee_damage
        self.heavy_melee_damage             = heavy_melee_damage
        self.bonus_melee_damage             = bonus_melee_damage
        self.bonus_heavy_melee_damage       = bonus_heavy_melee_damage
    
    def draw(self):
        st.write(f'bonus_bullet_damage: {self.bonus_bullet_damage}')


class Vitality:
    def __init__(   self,\
                    max_health:             float   = .0,\
                    health_regen:           float   = .0,\
                    out_of_combat_regen:    float   = .0,\
                    bullet_resist:          float   = .0,\
                    spirit_resist:          float   = .0,\
                    melee_resist:           float   = .0,\
                    crit_reduction:         float   = .0,\
                    move_speed:             float   = .0,\
                    sprint_speed:           float   = .0,\
                    stamina_cooldown:       float   = .0,\
                    stamina_count:          int     =  0,):
        self.max_health                     = max_health
        self.health_regen                   = health_regen
        self.out_of_combat_regen            = out_of_combat_regen
        self.bullet_resist                  = bullet_resist
        self.spirit_resist                  = spirit_resist
        self.melee_resist                   = melee_resist
        self.crit_reduction                 = crit_reduction
        self.move_speed                     = move_speed
        self.sprint_speed                   = sprint_speed
        self.stamina_cooldown               = stamina_cooldown
        self.stamina_count                  = stamina_count
    
    def draw(self):
        pass

class Spirit:
    def __init__(   self,\
                    spirit_power:           int     = 0):
        self.spirit_power = spirit_power
    
    def draw(self):
        pass


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
    
    def draw(self):
        pass



class Character:
    def __init__(self, weapon: Weapon= Weapon(), vitality: Vitality= Vitality(), spirit: Spirit= Spirit(), growth: Growth= Growth()):
        self.weapon     = weapon
        self.vitality   = vitality
        self.spirit     = spirit
        self.growth     = growth

    def draw(self):
        self.weapon.draw()
        self.vitality.draw()
        self.spirit.draw()