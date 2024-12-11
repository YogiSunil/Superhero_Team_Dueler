import random

class Ability:
    def __init__(self, name, max_damage):
        '''Initialize the values passed into this method as instance variables.'''
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        '''Return a value between 0 and the value set by self.max_damage.'''
        # Pick a random value between 0 and self.max_damage
        return random.randint(0, self.max_damage)

if __name__ == "__main__":
    # Test the Ability class
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
