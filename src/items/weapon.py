import streamlit as st
from .item import Item, ConditionalProc
import stats

# 800
class CloseQuarter(Item, ConditionalProc):
    def __init__(self):
        super().__init__()
        self.name = "Close Quarter"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/close_quarters.webp"
        self.price = 800

    @classmethod
    def register(cls, inventory):
        if PointBlank.exists(inventory):
            return
        super().register(inventory)

    def apply_stats(self, character: stats.Character):
        character.vitality.melee_resist = stats.add_multiplicative(character.vitality.melee_resist, 0.2)
        if self.enable:
            character.weapon.bonus_bullet_damage += 0.2

    def show_cond_window(self):
        self.enable = st.toggle("Enable Passive", True)
        
class ExtendedMagazine(Item):
    def __init__(self):
        self.name = "Extended Magazine"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/basic_magazine.webp"
        self.price = 800

    def apply_stats(self, character: stats.Character):
        character.weapon.bonus_ammo_perc += 0.3
        character.weapon.bonus_bullet_damage += 0.08

    @classmethod
    def register(cls, inventory):
        if TitanicMagazine.exists(inventory) or \
           EscalatingResilience.exists(inventory):
            return
        super().register(inventory)
    
class HeadshotBooster(Item):
    def __init__(self):
        self.name = "Headshot Booster"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/headshot_booster.webp"
        self.price = 800

    def apply_stats(self, character: stats.Character):
        character.vitality.max_health += 30

class HighVelocityRounds(Item):
    def __init__(self):
        self.name = "High Velocity Rounds"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/high_velocity_rounds.webp"
        self.price = 800

    @classmethod
    def register(cls, inventory):
        if ExpressShot.exists(inventory) or\
           ArmorPiercingRounds.exists(inventory):
            return
        super().register(inventory)


class MonsterRounds(Item):
    def __init__(self):
        self.name = "Monster Rounds"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/monster_rounds.webp"
        self.price = 800

    @classmethod
    def register(cls, inventory):
        if CultistSacrifice.exists(inventory): 
            return
        super().register(inventory)


class RapidRounds(Item):
    def __init__(self):
        self.name = "Rapid Rounds"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/rapid_rounds.webp"
        self.price = 800
    
    @classmethod
    def register(cls, inventory):
        if SwiftStriker.exists(inventory) or\
           BurstFire.exists(inventory):
           return
        super().register(inventory)


class RestorativeShot(Item):
    def __init__(self):
        self.name = "Restorative Shot"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/restorative_shot.webp"
        self.price = 800


# ===== 1600 =====

class ActiveReload(Item):
    def __init__(self):
        self.name = "Active Reload"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/active_reload.webp"
        self.price = 1600


class Fleetfoot(Item):
    def __init__(self):
        self.name = "Fleetfoot"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/fleetfoot.webp"
        self.price = 1600


class IntensifyingMagazine(Item):
    def __init__(self):
        self.name = "Intensifying Magazine"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/intensifying_magazine.webp"
        self.price = 1600


class KineticDash(Item):
    def __init__(self):
        self.name = "Kinetic Dash"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/kinetic_dash.webp"
        self.price = 1600


class LongRange(Item):
    def __init__(self):
        self.name = "Long Range"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/long_range.webp"
        self.price = 1600

    @classmethod
    def register(cls, inventory):
        if Sharpshooter.exists(inventory):
            return
        super().register(inventory)

class MeleeCharge(Item):
    def __init__(self):
        self.name = "Melee Charge"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/melee_charge.webp"
        self.price = 1600

    @classmethod
    def register(cls, inventory):
        if CrushingFists.exists(inventory):
            return
        super().register(inventory)

class MysticShot(Item):
    def __init__(self):
        self.name = "Mystic Shot"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/mystic_shot.webp"
        self.price = 1600

class OpeningRounds(Item):
    def __init__(self):
        self.name = "Opening Rounds"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/opening_rounds.webp"
        self.price = 1600
    
class RechargingRush(Item):
    def __init__(self):
        self.name = "Recharging Rush"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/recharging_rounds.webp"
        self.price = 1600

class SlowingBullets(Item):
    def __init__(self):
        self.name = "Slowing Bullets"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/slowing_bullets.webp"
        self.price = 1600
    
    @classmethod
    def register(cls, inventory):
        if WeightedShots.exists(inventory):
            return
        super().register(inventory)

class SpiritShredderBullets(Item):
    def __init__(self):
        self.name = "Spirit Shredder Bullets"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/spirit_shredder_bullets.webp"
        self.price = 1600
    
    @classmethod
    def register(cls, inventory):
        if SpiritRend.exists(inventory):
            return
        super().register(inventory)

class SplitShot(Item):
    def __init__(self):
        self.name = "Split Shot"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/split_shot.webp"
        self.price = 1600

class Stalker(Item):
    def __init__(self):
        self.name = "Stalker"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/backstabber.webp"
        self.price = 1600

class SwiftStriker(Item):
    def __init__(self):
        self.name = "Swift Striker"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/swift_striker.webp"
        self.price = 1600
    
    @classmethod
    def register(cls, inventory):
        RapidRounds.remove(inventory)
        super().register(inventory)


class TitanicMagazine(Item):
    def __init__(self):
        self.name = "Titanic Magazine"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/titanic_magazine.webp"
        self.price = 1600

    @classmethod
    def register(cls, inventory):
        ExtendedMagazine.remove(inventory)
        super().register(inventory)


class WeakeningHeadshot(Item):
    def __init__(self):
        self.name = "Weakening Headshot"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/weakening_headshot.webp"
        self.price = 1600

    @classmethod
    def register(cls, inventory):
        if CripplingHeadshot.exists(inventory):
            return
        super().register(inventory)


# ===== 3200 =====

class AlchemicalFire(Item):
    def __init__(self):
        self.name = "Alchemical Fire"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/alchemical_fire.webp"
        self.price = 3200

class BallisticEnchantment(Item):
    def __init__(self):
        self.name = "Ballistic Enchantment"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/long_range.webp"
        self.price = 3200
    
    @classmethod
    def register(cls, inventory):
        ExtendedMagazine.remove(inventory)
        super().register(inventory)

class Berserker(Item):
    def __init__(self):
        self.name = "Berserker"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/berserker.webp"
        self.price = 3200

class BloodTribute(Item):
    def __init__(self):
        self.name = "Blood Tribute"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/blood_tribute.webp"
        self.price = 3200

class BurstFire(Item):
    def __init__(self):
        self.name = "Burst Fire"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/burst_fire.webp"
        self.price = 3200

    @classmethod
    def register(cls, inventory):
        RapidRounds.remove(inventory)
        super().register(inventory)

class CultistSacrifice(Item):
    def __init__(self):
        self.name = "Cultist Sacrifice"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/cultist_sacrifice.webp"
        self.price = 3200

    @classmethod
    def register(cls, inventory):
        MonsterRounds.remove(inventory)
        super().register(inventory)

class EscalatingResilience(Item):
    def __init__(self):
        self.name = "Escalating Resilience"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/escalating_resilience.webp"
        self.price = 3200

    @classmethod
    def register(cls, inventory):
        ExtendedMagazine.remove(inventory)
        super().register(inventory)

class ExpressShot(Item):
    def __init__(self):
        self.name = "Express Shot"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/express_shot.webp"
        self.price = 3200

    @classmethod
    def register(cls, inventory):
        HighVelocityRounds.remove(inventory)
        super().register(inventory)

class Headhunter(Item):
    def __init__(self):
        self.name = "Headhunter"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/headhunter.webp"
        self.price = 3200
    
    @classmethod
    def register(cls, inventory):
        HeadshotBooster.remove(inventory)
        super().register(inventory)

class HeroicAura(Item):
    def __init__(self):
        self.name = "Heroic Aura"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/heroic_aura.webp"
        self.price = 3200

class HollowPoint(Item):
    def __init__(self):
        self.name = "Hollow Point"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/hollow_point.webp"
        self.price = 3200

class HuntersAura(Item):
    def __init__(self):
        self.name = "Hunter's Aura"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/hunters_aura.webp"
        self.price = 3200


class PointBlank(Item):
    def __init__(self):
        self.name = "Point Blank"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/point_blank.webp"
        self.price = 3200

    @classmethod
    def register(cls, inventory):
        CloseQuarter.remove(inventory)
        super().register(inventory)


class Sharpshooter(Item):
    def __init__(self):
        self.name = "Sharpshooter"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/sharp_shooter.webp"
        self.price = 3200

    @classmethod
    def register(cls, inventory):
        LongRange.remove(inventory)
        super().register(inventory)

class SpiritRend(Item):
    def __init__(self):
        self.name = "Spirit Rend"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/spellslinger_headshots.webp"
        self.price = 3200

    @classmethod
    def register(cls, inventory):
        SpiritShredderBullets.remove(inventory)
        super().register(inventory)

class TeslaBullets(Item):
    def __init__(self):
        self.name = "Tesla Bullets"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/tesla_bullets.webp"
        self.price = 3200

    @classmethod
    def register(cls, inventory):
        if Capacitor.exists(inventory):
            return

        super().register(inventory)

class ToxicBullets(Item):
    def __init__(self):
        self.name = "Toxic Bullets"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/toxic_bullets.webp"
        self.price = 3200

class WeightedShots(Item):
    def __init__(self):
        self.name = "Weighted Shots"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/weighted_shots.webp"
        self.price = 3200

    @classmethod
    def register(cls, inventory):
        SlowingBullets.remove(inventory)
        super().register(inventory)

# ===== 6400 =====
class ArmorPiercingRounds(Item):
    def __init__(self):
        self.name = "Armor Piercing Rounds"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/armor_piercing_rounds.webp"
        self.price = 6400

    @classmethod
    def register(cls, inventory):
        HighVelocityRounds.remove(inventory)
        super().register(inventory)

class Capacitor(Item):
    def __init__(self):
        self.name = "Capacitor"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/capacitor.webp"
        self.price = 6400

    @classmethod
    def register(cls, inventory):
        TeslaBullets.remove(inventory)
        super().register(inventory)

class CripplingHeadshot(Item):
    def __init__(self):
        self.name = "Crippling Headshot"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/crippling_headshot.webp"
        self.price = 6400

    @classmethod
    def register(cls, inventory):
        WeakeningHeadshot.remove(inventory)
        super().register(inventory)

class CrushingFists(Item):
    def __init__(self):
        self.name = "Crushing Fists"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/crushing_fists.webp"
        self.price = 6400

    @classmethod
    def register(cls, inventory):
        MeleeCharge.remove(inventory)
        super().register(inventory)

class Frenzy(Item):
    def __init__(self):
        self.name = "Frenzy"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/frenzy.webp"
        self.price = 6400


class GlassCannon(Item):
    def __init__(self):
        self.name = "Glass Cannon"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/glass_cannon.webp"
        self.price = 6400


class LuckyShot(Item):
    def __init__(self):
        self.name = "Lucky Shot"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/lucky_shot.webp"
        self.price = 6400


class Ricochet(Item):
    def __init__(self):
        self.name = "Ricochet"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/ricochet.webp"
        self.price = 6400

class ShadowWeave(Item):
    def __init__(self):
        self.name = "Shadow Weave"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/shadow_weave.webp"
        self.price = 6400

class Silencer(Item):
    def __init__(self):
        self.name = "Silencer"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/silencer.webp"
        self.price = 6400

class Spellslinger(Item):
    def __init__(self):
        self.name = "Spellslinger"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/spell_slinger.webp"
        self.price = 6400

class SpiritualOverflow(Item):
    def __init__(self):
        self.name = "Spiritual Overflow"
        self.icon = "https://game.deadlock.coach/vpk/panorama/images/items/weapon/spiritual_overflow.webp"
        self.price = 6400




