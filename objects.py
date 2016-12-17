import arcade.key
import arcade.sound
from random import randint,random
from model_SongsCollection import SongsCollection
from botton import Botton,Screen

class World:
    def __init__(self, width, height):
        super(World, self).__init__()
        self.width = width
        self.height = height
        self.score=0
        self.life = 1
        #self.time = 5
        self.count = 0
        self.songs_collection = SongsCollection(self)
        self.is_gen_new_songs = True
        self.is_press = False
        self.mouse_x = 0
        self.mouse_y = 0
        self.status_game = 1
        self.status_start = -1
        self.status_play = 1
        self.status_gameover = 2
        self.is_press_space = False

    def status_screen(self):
        if self.status_game == self.status_start:
            if self.is_press_space == True:
                self.status_game = self.status_play
                self.is_press_space = False


    def animate(self,delta):
        self.status_screen()
        self.get_screen()
        if self.is_gen_new_songs:
            self.gen_levels()
            self.gen_botton()
            self.play_sound()
            self.is_gen_new_songs = False
        self.mouse_detect()
        self.cal_score()


    def cal_score(self):
        if self.is_press :
            choose_choice = ""
            for button in self.bottons :
                if button.mouse_on :
                    choose_choice = button.text
            if self.life > 0:
                if choose_choice != "":
                    if choose_choice == self.true_song:
                        self.score += 1
                    else :
                        self.life -= 1
                    self.pause_sound()
                    self.is_gen_new_songs = True
            if self.life <= 0:
                self.status_game = self.status_gameover

            self.is_press = False

    def mouse_detect(self):
        for i in range (0,len(self.bottons)):
            self.bottons[i].mouse_on = False
            if self.bottons[i].center_x - 235 <= self.mouse_x <= self.bottons[i].center_x + 235  :
                if self.bottons[i].center_y - 75 <= self.mouse_y <= self.bottons[i].center_y + 75 :
                    self.bottons[i].mouse_on = True

    def gen_botton(self):
        self.bottons = [Botton(300,400,self.choices[0]),Botton(300,200,self.choices[1]),Botton(900,200,self.choices[2]),Botton(900,400,self.choices[3])]

    def get_screen(self):
        self.set_screen = Screen(600,350)

    def pause_sound(self):
        self.player.pause()

    def play_sound(self):
        self.player = self.now_song.play()

    def gen_levels(self):
        self.songs_collection.get_songs_and_choices()
