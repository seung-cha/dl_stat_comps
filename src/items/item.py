from abc import ABC, abstractmethod
import streamlit as st
import stats

class Item(ABC):
    def __init__(self):
        super().__init__()
        self.name = None
        self.icon = None
        self.price = 0

    def draw(self) -> bool:
        # TODO: Change the button design
        return st.button(f"![{self.name}]({self.icon}) {self.name}")

    #@classmethod
    #@abstractmethod
    def apply_stats(self, character: stats.Character):
        pass

    @classmethod
    def exists(cls, inventory: list) -> bool:
        return any(isinstance(x, cls) for x in inventory)

    @classmethod
    def register(cls, inventory: list):
        if not cls.exists(inventory):
            cls.insert(inventory)
        else:
            cls.remove(inventory)

    @classmethod
    def insert(cls, inventory: list):
        inventory.append(cls())

    @classmethod
    def remove(cls, inventory: list):
        try:
            ind = [isinstance(item, cls) for item in inventory].index(True)
            inventory.pop(ind)
        except:
            return


class ConditionalProc(ABC):
    """
    For items that have conditional effects, draw a window to enable/disable the effects.
    """
    def __init__(self):
        super().__init__()
        self.enable = True

    def show_cond_window(self):
        self.enable = st.toggle("Enable Effect", True, key= type(self))
