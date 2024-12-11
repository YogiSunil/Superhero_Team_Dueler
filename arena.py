from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        '''Initialize the Arena with two teams.'''
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")

    def create_ability(self):
        '''Prompt the user to create an ability.'''
        name = input("What is the ability name? ")
        max_damage = input("What is the max damage of the ability? ")
        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt the user to create a weapon.'''
        name = input("What is the weapon name? ")
        max_damage = input("What is the max damage of the weapon? ")
        return Weapon(name, max_damage)

    def create_armor(self):
        '''Prompt the user to create armor.'''
        name = input("What is the armor name? ")
        max_block = input("What is the max block of the armor? ")
        return Armor(name, max_block)

    def create_hero(self):
        '''Prompt the user to create a hero.'''
        name = input("Hero's name: ")
        hero = Hero(name)
        while True:
            choice = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done\nYour choice: ")
            if choice == "1":
                hero.add_ability(self.create_ability())
            elif choice == "2":
                hero.add_weapon(self.create_weapon())
            elif choice == "3":
                hero.add_armor(self.create_armor())
            elif choice == "4":
                break
        return hero

    def build_team_one(self):
        '''Prompt the user to build team one.'''
        num_heroes = int(input("How many heroes on Team One? "))
        for _ in range(num_heroes):
            self.team_one.add_hero(self.create_hero())

    def build_team_two(self):
        '''Prompt the user to build team two.'''
        num_heroes = int(input("How many heroes on Team Two? "))
        for _ in range(num_heroes):
            self.team_two.add_hero(self.create_hero())

    def team_battle(self):
        '''Battle the two teams.'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Show stats for both teams.'''
        self.team_one.stats()
        self.team_two.stats()

        # Surviving heroes
        print("Surviving heroes:")
        for hero in self.team_one.heroes:
            if hero.is_alive():
                print(f"{hero.name} from Team One")

        for hero in self.team_two.heroes:
            if hero.is_alive():
                print(f"{hero.name} from Team Two")

if __name__ == "__main__":
    game_is_running = True
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play again? (Y/N): ")
        if play_again.lower() == 'n':
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
