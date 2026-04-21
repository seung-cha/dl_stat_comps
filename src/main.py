import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import items
import stats
from shop import Shop
from char_select import CharacterSelection
from copy import deepcopy
#from session_context import SessionContext

st.title("WIP")

boon_souls_req = [
    600, 900, 1200, 1500, 2100, 2800,\
    3600, 4400, 5200, 6000, 6800, 7700,\
    8600, 9600, 10600, 11600, 12600, 13800,\
    15600, 17600, 19600, 21600, 23600, 25600,\
    27600, 29600, 31600, 33600, 35600, 37600,\
    39600, 41600, 43600, 45600, 47600, 49600,
]

boon_max_lvl = 35

weapon_investment = [0, 0.07, 0.09, 0.13, 0.2, 0.49, 0.6, 0.8, 0.95, 1.15, 1.35]
weapon_souls_req = [0, 800, 1600, 2400, 3200, 4800, 7200, 9600, 1600, 22400, 28800]



# Init session context
# session keys:
#   * inventory: list[items.Item]
#   * hero: stats.HeroUnit 
#   * selected_hero: stats.HeroUnit (st.menu_button returns None every time render updates.

if 'inventory' not in st.session_state:
    st.session_state.inventory = list()

if 'hero' not in st.session_state: # Default character to start the session with
    st.session_state.hero = stats.get_abrams()

char_select = CharacterSelection()
char_select.draw()

# deepcopy to keep the selected hero readonly
hero = deepcopy(st.session_state.hero)
st.write(f"selected: {hero}")

s = Shop()
s.draw()

# Draw item cond windows
for item in st.session_state.inventory:
    item: items.ConditionalProc
    if isinstance(item, items.ConditionalProc):
        item.show_cond_window()


for item in st.session_state.inventory:
    item: items.Item
    item.apply_stats(hero.stats)

hero.stats.draw()



#st.write(f"Bullet Damage: {char.weapon.base_bullet_damage}")


