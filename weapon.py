from ability import Ability
import random

class Weapon(Ability):
    def attack(self):
        """Return a random damage value between half of max_damage and max_damage."""
        half_damage = self.max_damage // 2
        return random.randint(half_damage, self.max_damage)
