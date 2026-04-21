import streamlit as st
import stats


class CharacterSelection:

    def draw(self):
        st.session_state.selected_hero = st.menu_button("Character", options= [stats.get_abrams(), stats.get_dummy()])

        if st.session_state.selected_hero is not None:
            st.session_state.hero = st.session_state.selected_hero