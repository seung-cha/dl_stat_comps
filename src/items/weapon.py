from .item import Item, ConditionalProc
import stats
import streamlit as st

# 800
class CloseQuarter(Item, ConditionalProc):
    def __init__(self):
        super().__init__()
        self.name = "Close Quarter"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/close_quarters.webp"
        self.price = 800

    @classmethod
    def apply_stats(self, character: stats.Character):
        character.vitality.melee_resist += 0.2
        if self.enable:
            character.weapon.base_bullet_damage += 0.2

    @classmethod
    def show_cond_window(self):
        self.enable = st.toggle("Enable Close Quarter Extra Damage", True)
        

class ExtendedMagazine(Item):
    def __init__(self):
        self.name = "Extended Magazine"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/basic_magazine.webp"
        self.price = 800

    def apply_stats(self, character: stats.Character):
        character.weapon.ammo += 0.3
        character.weapon.base_bullet_damage += 0.08
    
class HeadshotBooster(Item):
    def __init__(self):
        self.name = "Headshot Booster"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/headshot_booster.webp"
        self.price = 800

    def apply_stats(self, character: stats.Character):
        character.vitality.max_health += 30



# close_quarter = Item(name= "Close Quarter", icon= "https://game.deadlock.coach/vpk/panorama/images/items/weapon/close_quarters.webp")

# extended_magazine = Item(name= "Extended Magazine", icon= "https://game.deadlock.coach/vpk/panorama/images/items/weapon/basic_magazine.webp")

# headshot_booster = Item(name= "Headshot Booster", icon= "https://game.deadlock.coach/vpk/panorama/images/items/weapon/headshot_booster.webp")


