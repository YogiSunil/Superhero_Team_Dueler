import random

class Ability:
    def __init__(self, name, max_damage):
        '''Create instance variables:
          name: String
          max_damage: Integer
        '''
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        '''Return a random value between 0 and the value set by self.max_damage.'''
        return random.randint(0, self.max_damage)
