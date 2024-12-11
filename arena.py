from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one = []
        self.team_two = []

    def build_team_one(self):
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero_name = input(f"Hero {i+1} name: ")
            hero = Hero(hero_name)
            self.add_items(hero)
            self.team_one.append(hero)

    def build_team_two(self):
        while True:
            try:
                numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
                if numOfTeamMembers <= 0:
                    print("Please enter a positive number greater than 0.")
                    continue
                break  # Exit loop if valid input is provided
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        for i in range(numOfTeamMembers):
            hero_name = input(f"Hero {i+1} name: ")
            hero = Hero(hero_name)
            self.add_items(hero)
            self.team_two.append(hero)

    def add_items(self, hero):
        while True:
            print("[1] Add ability")
            print("[2] Add weapon")
            print("[3] Add armor")
            print("[4] Done adding items")
            choice = input("Your choice: ")

            if choice == '1':
                ability = input("Enter ability name: ")
                hero.add_ability(ability)
            elif choice == '2':
                weapon_name = input("What is the weapon name? ")
                damage = int(input("What is the damage of the weapon? "))
                hero.add_weapon(weapon_name, damage)
            elif choice == '3':
                armor_name = input("What is the armor name? ")
                defense_value = int(input("What is the defense value of the armor? "))
                hero.add_armor(armor_name, defense_value)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def show_teams(self):
        print("\nTeam One:")
        for hero in self.team_one:
            hero.show()

        print("\nTeam Two:")
        for hero in self.team_two:
            hero.show()


# Running the arena
arena = Arena()

# Building Team One
arena.build_team_one()

# Building Team Two
arena.build_team_two()

# Display the teams
arena.show_teams()