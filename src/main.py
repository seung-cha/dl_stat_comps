import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import items
from shop import Shop
#from session_context import SessionContext

st.title("WIP. Temporary using Billy's data")

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
if 'inventory' not in st.session_state:
    st.session_state.inventory = list()


s = Shop()
s.draw()


