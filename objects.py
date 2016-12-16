import arcade.key
import arcade.sound
from random import randint,random
from model_SongsCollection import SongsCollection
from botton import Botton

class World:
    NUM_HEART = 3
    def __init__(self, width, height):
        super(World, self).__init__()
        self.width = width
        self.height = height
        self.score=0
        self.life = 3
        #self.time = 5
        self.count = 0
        self.songs_collection = SongsCollection(self)
        self.i = 0
        self.is_press = False
        self.mouse_x = 0
        self.mouse_y = 0

    def animate(self,delta):
        if self.i == 0:
            self.gen_levels()
            self.gen_botton()
            self.play_sound()
            print (self.i)
        self.i = 1
        self.mouse_detect()
        self.cal_score()

    def cal_score(self):
        if self.is_press :
            choose_choice = ""
            for button in self.bottons :
                if button.mouse_on :
                    choose_choice = button.text
            if choose_choice == self.true_song:
                self.score += 1
            self.is_press = False

    def mouse_detect(self):
        for i in range (0,len(self.bottons)):
            self.bottons[i].mouse_on = False
            if self.bottons[i].center_x - 235 <= self.mouse_x <= self.bottons[i].center_x + 235  :
                if self.bottons[i].center_y - 75 <= self.mouse_y <= self.bottons[i].center_y + 75 :
                    self.bottons[i].mouse_on = True

    def gen_botton(self):
        self.bottons = [Botton(300,400,self.choices[0]),Botton(300,200,self.choices[1]),Botton(900,200,self.choices[2]),Botton(900,400,self.choices[3])]

    def play_sound(self):
        arcade.sound.play_sound(self.now_song)

    def gen_levels(self):
        self.songs_collection.get_songs_and_choices()
