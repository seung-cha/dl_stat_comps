import items
import stats
import streamlit as st
from dataclasses import dataclass

# TODO use or discard

@dataclass
class SessionContext:
    def __str__(self):
        return f'SessionContext{self.index}'
    
    def __init__(self, index: int= 0):
        self.index = index
        self.character_stats = stats.Character()
        self.items: list[items.Item] = list()

        self.close_quarter = items.weapon.CloseQuarter()
        self.headshot_booster = items.weapon.HeadshotBooster()
        self.extended_mag = items.weapon.ExtendedMagazine()




    

    def draw(self):
        if self.close_quarter.draw():
            st.session_state.inventory.append(1)
        
        if self.headshot_booster.draw():
            st.session_state.inventory.append(2)

        if self.extended_mag.draw():
            st.session_state.inventory.append(3)


        st.write(st.session_state.inventory)
        


