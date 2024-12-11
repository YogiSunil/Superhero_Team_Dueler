import random

class Armor:
    def __init__(self, name, max_block):
        '''Create instance variables:
          name: String
          max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        '''Return a random value between 0 and the value set by self.max_block.'''
        return random.randint(0, self.max_block)
