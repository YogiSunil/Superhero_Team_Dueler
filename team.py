from hero import Hero

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def attack(self, opponent):
        total_damage = sum([hero.attack() for hero in self.heroes if hero.is_alive])
        opponent.receive_damage(total_damage)

    def receive_damage(self, damage):
        for hero in self.heroes:
            if hero.is_alive:
                hero.receive_damage(damage)

    def revive_heroes(self):
        for hero in self.heroes:
            hero.revive()

    def stats(self):
        total_kills = sum([hero.kills for hero in self.heroes])
        total_deaths = sum([hero.deaths for hero in self.heroes])
        print(f"Total Kills: {total_kills}, Total Deaths: {total_deaths}")
