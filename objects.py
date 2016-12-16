import arcade.key
import arcade.sound
from random import randint,random
from model_SongsCollection import SongsCollection

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
        self.songs_collection = SongsCollection(self)
        self.i = 0

    def animate(self,delta):

        if self.i == 0:
            self.gen_levels()
            self.play_sound()
            print (self.i)
        self.i = 1

    def play_sound(self):
        arcade.sound.play_sound(self.now_song)

    def gen_levels(self):
        self.songs_collection.get_songs_and_choices()
