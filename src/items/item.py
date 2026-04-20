from abc import ABC, abstractmethod
import streamlit as st
import stats

class Item(ABC):
    def __init__(self):
        self.name = None
        self.icon = None
        self.price = 0
        super().__init__()

    def draw(self) -> bool:
        # TODO: Change the button design
        return st.button(f"![{self.name}]({self.icon}) {self.name}")
    
    @classmethod
    @abstractmethod
    def apply_stats(self, character: stats.Character):
        pass


class ConditionalProc(ABC):
    """
    For items that have conditional effects, draw a window to enable/disable the effects.
    """
    def __init__(self):
        self.enable = True
        super().__init__()

    @classmethod
    @abstractmethod
    def show_cond_window(self):
        pass
