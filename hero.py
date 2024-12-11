from ability import Ability
from weapon import Weapon
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        '''Initialize the hero with a name and starting health.'''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        '''Add an ability to the hero.'''
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        '''Add a weapon to the hero.'''
        self.add_ability(weapon)

    def add_armor(self, armor):
        '''Add armor to the hero.'''
        self.armors.append(armor)

    def attack(self):
        '''Calculate the total attack damage from all abilities.'''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        '''Calculate the total block value from all armors.'''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        '''Update the hero's health to reflect the damage taken.'''
        self.current_health -= damage

    def is_alive(self):
        '''Return True if the hero is alive, otherwise False.'''
        return self.current_health > 0

    def fight(self, opponent):
        '''Engage in a fight between this hero and an opponent.'''
        while self.is_alive() and opponent.is_alive():
            damage_to_opponent = self.attack() - opponent.defend()
            damage_to_self = opponent.attack() - self.defend()
            if damage_to_opponent > 0:
                opponent.take_damage(damage_to_opponent)
            if damage_to_self > 0:
                self.take_damage(damage_to_self)

        if self.is_alive():
            self.kills += 1
            opponent.deaths += 1
        else:
            opponent.kills += 1
            self.deaths += 1
