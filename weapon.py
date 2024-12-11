from ability import Ability
import random
class Weapon(Ability):
    def attack(self):
        '''Return a random value between half and full damage.'''
        return random.randint(self.max_damage // 2, self.max_damage)
