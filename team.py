import random

class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes '''
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        ''' Add Hero object to self.heroes '''
        self.heroes.append(hero)

    def remove_hero(self, name):
        ''' Remove hero from heroes list. If Hero isn't found, return 0. '''
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        ''' Print all heroes to the console '''
        for hero in self.heroes:
            print(hero.name)

    def revive_heroes(self, health=100):
        ''' Reset all heroes' health to starting_health '''
        for hero in self.heroes:
            hero.health = hero.starting_health

    def stats(self):
        ''' Print team statistics (Kill/Death ratio) '''
        for hero in self.heroes:
            if hero.deaths > 0:
                kd_ratio = hero.kills / hero.deaths
            else:
                kd_ratio = hero.kills  # If no deaths, just show kills
            print(f"{hero.name} Kill/Deaths: {kd_ratio}")

    def attack(self, other_team):
        ''' Battle each team against each other. '''
        living_heroes = [hero for hero in self.heroes if hero.health > 0]
        living_opponents = [hero for hero in other_team.heroes if hero.health > 0]

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            hero = random.choice(living_heroes)  # Randomly select a hero
            opponent = random.choice(living_opponents)  # Randomly select an opponent

            hero.fight(opponent)  # They fight
            if hero.health <= 0:
                living_heroes.remove(hero)  # Hero died
            if opponent.health <= 0:
                living_opponents.remove(opponent)  # Opponent died
