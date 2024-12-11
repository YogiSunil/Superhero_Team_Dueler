from ability import Ability
from weapon import Weapon

class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.starting_health = health  # To keep track of original health
        self.deaths = 0
        self.kills = 0
        # Add any other attributes you already have
        # ...

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount '''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths '''
        self.deaths += num_deaths

    def fight(self, opponent):
        '''Simulate fight and update stats'''
        if self.health > opponent.health:
            opponent.add_death(1)  # Opponent dies
            self.add_kill(1)  # Hero gets a kill
        elif self.health < opponent.health:
            self.add_death(1)  # Hero dies
            opponent.add_kill(1)  # Opponent gets a kill
        else:
            # If health is equal, nobody dies
            pass
