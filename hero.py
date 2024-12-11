from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        '''Add ability to abilities list.'''
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.'''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors.'''
        self.armors.append(armor)

    def defend(self, incoming_damage):
        '''Calculate the total block amount from all armor blocks.'''
        if self.current_health <= 0:
            return 0
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return min(incoming_damage, total_block)

    def take_damage(self, damage):
        '''Update self.current_health to reflect damage minus defense.'''
        defense = self.defend(damage)
        damage_taken = max(0, damage - defense)
        self.current_health -= damage_taken

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive.'''
        return self.current_health > 0

    def fight(self, opponent):
        '''Fight another hero until one is defeated.'''
        while self.is_alive() and opponent.is_alive():
            damage_to_opponent = self.attack()
            opponent.take_damage(damage_to_opponent)

            if opponent.is_alive():
                damage_to_self = opponent.attack()
                self.take_damage(damage_to_self)
            else:
                print(f"{self.name} won!")
                return

        print(f"{opponent.name} won!")
