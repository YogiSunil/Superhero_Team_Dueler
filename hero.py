from ability import Ability
from weapon import Weapon
from armor import Armor

class Hero:
    def __init__(self, name):
        self.name = name
        self.abilities = []
        self.weapons = []
        self.armors = []

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon_name, damage):
        self.weapons.append({"name": weapon_name, "damage": damage})

    def add_armor(self, armor_name, defense_value):
        self.armors.append({"name": armor_name, "defense_value": defense_value})

    def show(self):
        print(f"Hero Name: {self.name}")
        print("Abilities: ", self.abilities)
        print("Weapons: ", self.weapons)
        print("Armors: ", self.armors)
