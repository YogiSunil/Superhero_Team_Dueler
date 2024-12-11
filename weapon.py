class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = int(damage)

    def attack(self):
        return self.damage
