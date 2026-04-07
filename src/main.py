import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Using Billy as temp hero
# Support bullet dmg only for now


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
weapon_investment_cap = 11

boon_bonus = {
    'bullet_dmg': 0.17
}

billy = {
    'base_bullet_dmg': 6.3,
    'base_fire_rate': 11.76,
    'fire_rate' : 11.76,
    'bonus_boon_bullet_damage': 0,
    'bonus_shop_bullet_damage': 0,
    'bonus_invest_bullet_damage': 0,
    'combined_base_dmg': 0,
    'total_bullet_damage': 0,
}

lvl = 0
invest_lvl = 0
current_souls = 0
current_lvl = 0
bonus_shop_weapon_dmg = 0


#### Base Dmg Calc

# Boon lvl input
current_lvl = st.number_input("Current Level (Boons)", 0, boon_max_lvl)

if current_lvl == 0:
    current_souls = 0
else:
    current_souls = boon_souls_req[current_lvl]

# Shop investment 
st.write(f"You currently have {current_souls} souls to spare")

invest_lvl = st.select_slider('Weapon Investment', options=list(range(weapon_investment_cap)), \
                format_func= lambda x: f"{weapon_souls_req[x]} ({weapon_investment[x] * 100}%)")

bonus_shop_weapon_dmg = st.number_input("Bonus Weapon Damage from Items (Percentage)", min_value= 0)

# Stats calc
billy['bonus_boon_bullet_damage'] = current_lvl * boon_bonus['bullet_dmg']
billy['combined_base_dmg'] = billy['base_bullet_dmg'] + billy['bonus_boon_bullet_damage']
billy['bonus_shop_bullet_damage'] = billy['combined_base_dmg'] * (bonus_shop_weapon_dmg / 100)
billy['bonus_invest_bullet_damage'] = billy['combined_base_dmg'] * weapon_investment[invest_lvl]

billy['total_bullet_damage'] = billy['combined_base_dmg'] + billy['bonus_shop_bullet_damage'] + billy['bonus_invest_bullet_damage']

# Show final bullet stats
st.write("raw damage output (base + boon bonus): ", billy['combined_base_dmg'])
st.write("Bonus Damage from investment: ", billy['bonus_invest_bullet_damage'])
st.write("Bonus damage from items: ", billy['bonus_shop_bullet_damage'])



###### Shred
# name, cost, shred percentage
shred_items = [
    ['Stalker', 1600, 0.06],
    ['Weakening Headshot', 1600, 0.13],
    ['Hollow Point', 3200, 0.09],
    ['Hunters Aura', 3200, 0.1],
    ['Hunters Aura (Alone)', 3200, 0.2],
    ['Crippling Headshot', 6400, 0.16]
]

total_shred = 0
souls_cost = 0
shred_bonus_damage = 0
# Calculate dmg shred
selected_shreds = st.segmented_control("Select shred items", selection_mode='multi', options= shred_items, \
                                       format_func= lambda x: f"{x[0]} (${x[1]}, {x[2]*100}%)") 

shred = 0
if len(selected_shreds) > 0:
    shred = 1 - selected_shreds[0][2]
    souls_cost = selected_shreds[0][1]

    for i in range(1, len(selected_shreds)):
        shred *= 1-selected_shreds[i][2]
        souls_cost += selected_shreds[i][1]

    shred = 1 - shred



# Show final shred stats
st.write("Total souls cost: ", souls_cost)
st.write("Total shred: ", shred * 100, "%")

# Calculate bonus dmg from shred
shred_bonus_damage = billy['total_bullet_damage'] * shred

# Final damage output
st.write("Final Output (against enemy with 0 resistance)")
st.write("Total Outgoing Bullet Damage (Without shred): ", billy['total_bullet_damage'])
st.write("Total Outgoing Bullet Damage (With shred): ", billy['total_bullet_damage'] + shred_bonus_damage)
st.write("Bonus bullet damage from shred: ", shred_bonus_damage)



# Plot

resistance = np.arange(0, 1, 0.05)
unshredded_dmg = (1 - resistance) * billy['total_bullet_damage']
shredded_dmg = (1 - resistance + shred) * billy['total_bullet_damage']
fig, ax = plt.subplots()
ax.plot(resistance * 100, unshredded_dmg)
ax.plot(resistance * 100, shredded_dmg)
ax.set_xlabel("Target Bullet Resistance (%)")
ax.set_ylabel("Outgoing bullet damage")
ax.legend(["Without shred", "With shred"])

st.pyplot(fig)

bonus_fire_rate = 0

bonus_fire_rate = st.number_input("Bonus Fire Rate (%)")

if bonus_fire_rate != 0:
    billy['fire_rate'] = billy['base_fire_rate'] + billy['base_fire_rate'] * (bonus_fire_rate / 100)

st.write("Theoretical DPS (without shred): ", billy['fire_rate'] * billy['total_bullet_damage'])
st.write("Theoretical DPS (with shred): ", billy['fire_rate'] * (billy['total_bullet_damage'] + shred_bonus_damage))

st.write("Diff: ", (billy['fire_rate'] * (billy['total_bullet_damage'] + shred_bonus_damage)) - (billy['fire_rate'] * billy['total_bullet_damage']))

st.write("\nDPS without bonus FR: ", billy['base_fire_rate'] * billy['total_bullet_damage'])
st.write("DPS without bonus FR (w Shred): ", billy['base_fire_rate'] * (billy['total_bullet_damage'] + shred_bonus_damage))
st.write("Diff: ", (billy['base_fire_rate'] * (billy['total_bullet_damage'] + shred_bonus_damage)) - (billy['base_fire_rate'] * billy['total_bullet_damage']))


# Plot 
fire_rate = np.arange(1, 3, 0.01)
unshred_dps = fire_rate * billy['total_bullet_damage'] * billy['base_fire_rate']
shred_dps = fire_rate * (billy['total_bullet_damage'] + shred_bonus_damage) * billy['base_fire_rate']
diff_dps = shred_dps - unshred_dps

fig, ax = plt.subplots()
ax.plot(fire_rate * 100, unshred_dps)
ax.plot(fire_rate * 100, shred_dps)

ax.set_xlabel("Fire rate (%)")
ax.set_ylabel("Hypothetical DPS")
ax.legend(['Unshredded', 'Shredded'])

st.pyplot(fig)



