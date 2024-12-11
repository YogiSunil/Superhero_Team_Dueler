from ability import Ability
from weapon import Weapon

class Hero:
    def __init__(self, name):
        self.name = name
        self.abilities = []

    def add_ability(self, ability):
        """Add an Ability to the hero's abilities list."""
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        """Add a Weapon to the hero's abilities list."""
        self.abilities.append(weapon)

    def attack(self):
        """Calculate the total damage from all abilities."""
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

if __name__ == "__main__":
    # Test Hero functionality
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    ability = Ability("Super Strength", 50)

    hero.add_ability(ability)
    hero.add_weapon(weapon)

    print(f"{hero.name} attacks with total damage: {hero.attack()}")
