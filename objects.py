import arcade.key
from random import randint,random
class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0


class World:
    NUM_HEART = 3
    def __init__(self, width, height):
        super(World, self).__init__()
        self.width = width
        self.height = height
        self.score=0
        self.life = 3
        self.time = 5
        self.count = 0
        
