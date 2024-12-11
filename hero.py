# hero.py
import random

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          name: String
          starting_health: Integer
          current_health: Integer
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.'''
        
        # Calculate total health to determine the chance of winning
        total_health = self.starting_health + opponent.starting_health
        self_win_chance = self.starting_health / total_health
        opponent_win_chance = opponent.starting_health / total_health
        
        # Randomly decide the winner based on health
        if random.random() < self_win_chance:
            print(f"{self.name} defeats {opponent.name}!")
        else:
            print(f"{opponent.name} defeats {self.name}!")

if __name__ == "__main__":
    # If you run this file from the terminal, this block is executed.
    hero1 = Hero("Wonder Woman", 300)
    hero2 = Hero("Dumbledore", 250)

    hero1.fight(hero2)
