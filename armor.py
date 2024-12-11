import random

class Armor:
    def __init__(self, name, max_block):
        '''Create an armor with a name and a max block value.'''
        self.name = name
        self.max_block = int(max_block)

    def block(self):
        '''Return a random value between 0 and the max block.'''
        return random.randint(0, self.max_block)
