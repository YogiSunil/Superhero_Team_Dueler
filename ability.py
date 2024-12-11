import random

class Ability:
    def __init__(self, name, max_damage):
        '''Create an ability with a name and max damage.'''
        self.name = name
        self.max_damage = int(max_damage)

    def attack(self):
        '''Return a random value between 0 and the max damage.'''
        return random.randint(0, self.max_damage)
