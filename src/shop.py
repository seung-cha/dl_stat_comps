import items
import stats
import streamlit as st
from dataclasses import dataclass

@dataclass
class Shop:    
    def __init__(self, index: int= 0):
        self.close_quarter = items.weapon.CloseQuarter()
        self.headshot_booster = items.weapon.HeadshotBooster()
        self.extended_mag = items.weapon.ExtendedMagazine()

    def draw(self):
        if self.close_quarter.draw():
            self.register(type(self.close_quarter))
        
        if self.headshot_booster.draw():
            self.register(type(self.headshot_booster))


        if self.extended_mag.draw():
            self.register(type(self.extended_mag))


        st.write(st.session_state.inventory)
    

    # TODO: Refine
    def register(self, item_class):
        if not any(isinstance(x, item_class) for x in st.session_state.inventory):
            self.insert(item_class)
        else:
            self.remove(item_class)

    def insert(self, item_class):
        if not any(isinstance(x, item_class) for x in st.session_state.inventory):
            st.session_state.inventory.append(item_class())

    def remove(self, item_class):
        try:
            ind = [isinstance(item, item_class) for item in st.session_state.inventory].index(True)
            st.session_state.inventory.pop(ind)
        except:
            return

    



