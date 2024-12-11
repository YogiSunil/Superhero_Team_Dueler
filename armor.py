class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = int(defense)

    def defend(self):
        return self.defense
