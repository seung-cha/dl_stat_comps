import items
import stats
import streamlit as st
from dataclasses import dataclass

@dataclass
class Shop:    
    def __init__(self, index: int= 0):
        self.weapon_items: list[items.Item] = [
            # 800   
            items.weapon.CloseQuarter()             ,                             
            items.weapon.ExtendedMagazine()         ,           
            items.weapon.HeadshotBooster()          ,      
            items.weapon.HighVelocityRounds()       ,         
            items.weapon.MonsterRounds()            ,    
            items.weapon.RapidRounds()              ,
            items.weapon.RestorativeShot()          ,
            # 1600  
            items.weapon.ActiveReload()             ,
            items.weapon.Fleetfoot()                ,
            items.weapon.IntensifyingMagazine()     ,       
            items.weapon.KineticDash()              ,
            items.weapon.LongRange()                ,
            items.weapon.MeleeCharge()              ,
            items.weapon.MysticShot()               ,
            items.weapon.OpeningRounds()             ,
            items.weapon.RechargingRush()           ,
            items.weapon.SlowingBullets()           ,
            items.weapon.SpiritShredderBullets()    ,
            items.weapon.SplitShot()                ,
            items.weapon.Stalker()                  ,   
            items.weapon.SwiftStriker()             ,
            items.weapon.TitanicMagazine()          ,   
            items.weapon.WeakeningHeadshot()        ,
            # 3200  
            items.weapon.AlchemicalFire()           ,
            items.weapon.BallisticEnchantment()     ,      
            items.weapon.Berserker()                ,
            items.weapon.BloodTribute()             ,
            items.weapon.BurstFire()                ,
            items.weapon.CultistSacrifice()         ,
            items.weapon.EscalatingResilience()     ,
            items.weapon.ExpressShot()              ,
            items.weapon.Headhunter()               ,
            items.weapon.HeroicAura()               ,
            items.weapon.HollowPoint()              ,
            items.weapon.HuntersAura()              ,
            items.weapon.PointBlank()               ,
            items.weapon.Sharpshooter()             ,
            items.weapon.SpiritRend()               ,
            items.weapon.TeslaBullets()             ,
            items.weapon.ToxicBullets()             ,
            items.weapon.WeightedShots()             ,
            # 6400  
            items.weapon.ArmorPiercingRounds()      ,
            items.weapon.Capacitor()                ,
            items.weapon.CripplingHeadshot()        ,
            items.weapon.CrushingFists()            ,
            items.weapon.Frenzy()                   ,
            items.weapon.GlassCannon()              ,   
            items.weapon.LuckyShot()                ,  
            items.weapon.Ricochet()                 ,
            items.weapon.ShadowWeave()              ,
            items.weapon.Silencer()                 ,
            items.weapon.Spellslinger()             ,
            items.weapon.SpiritualOverflow()        ,           
        ]       

    def draw(self):

        with st.container(horizontal= True):
            for item in self.weapon_items:
                if item.draw():
                    item.register(st.session_state.inventory)


        st.write(st.session_state.inventory)
    

    def exists(self, item_class) -> bool:
        return any(isinstance(x, item_class) for x in st.session_state.inventory)

    def register(self, item_class):
        if not self.exists(item_class):
            self.insert(item_class)
        else:
            self.remove(item_class)

    def insert(self, item_class):
        st.session_state.inventory.append(item_class())

    def remove(self, item_class):
        try:
            ind = [isinstance(item, item_class) for item in st.session_state.inventory].index(True)
            st.session_state.inventory.pop(ind)
        except:
            return

    



