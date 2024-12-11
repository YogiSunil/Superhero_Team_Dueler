from hero import Hero
import random
class Team:
    def __init__(self, name):
        '''Initialize the team with a name.'''
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        '''Add a hero to the team.'''
        self.heroes.append(hero)

    def remove_hero(self, name):
        '''Remove a hero from the team by name.'''
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return hero
        return None

    def view_all_heroes(self):
        '''Print the names of all heroes on the team.'''
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        '''Attack the opposing team.'''
        while any(hero.is_alive() for hero in self.heroes) and any(hero.is_alive() for hero in other_team.heroes):
            attacker = random.choice([hero for hero in self.heroes if hero.is_alive()])
            defender = random.choice([hero for hero in other_team.heroes if hero.is_alive()])
            attacker.fight(defender)

    def revive_heroes(self):
        '''Revive all heroes to their starting health.'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        '''Print kill/death stats for each hero.'''
        for hero in self.heroes:
            print(f"{hero.name}: {hero.kills}/{hero.deaths}")
