import arcade.key
import arcade.sound
from random import randint,random
from model_SongsCollection import SongsCollection
from button import Button,Screen

class World:
    def __init__(self, width, height):
        super(World, self).__init__()
        self.width = width
        self.height = height
        self.score=0
        self.life = 1
        self.count = 0
        self.songs_collection = SongsCollection(self)
        self.is_gen_new_songs = True
        self.is_press = False
        self.mouse_x = 0
        self.mouse_y = 0
        self.status_game = -1
        self.status_start = -1
        self.status_play = 1
        self.status_gameover = 2
        self.get_screen()
        self.draw_button_screen()


    def status_screen(self):
        if self.status_game == self.status_start:
            if self.is_start_press :
                if self.is_press:
                    self.status_game = self.status_play
                    self.is_start_press = False

    def animate(self,delta):
        if self.is_gen_new_songs:
            self.gen_levels()
            self.gen_button()
            self.play_sound()
            self.is_gen_new_songs = False
        self.mouse_detect()
        self.cal_score()

    def cal_score(self):
        if self.is_press :
            choose_choice = ""
            for button in self.buttons :
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
                self.pause_sound()
                self.is_gen_new_songs = False
            self.is_press = False

    def mouse_detect(self):
        for i in range (0,len(self.buttons)):
            self.buttons[i].mouse_on = False
            if self.buttons[i].center_x - 235 <= self.mouse_x <= self.buttons[i].center_x + 235  :
                if self.buttons[i].center_y - 75 <= self.mouse_y <= self.buttons[i].center_y + 75 :
                    self.buttons[i].mouse_on = True

    def mouse_detect_start_button(self):
        self.is_start_press = False
        if self.sc_game_start_button_unpress.center_x - 200 <= self.mouse_x <= self.sc_game_start_button_unpress.center_x + 200 :
            if self.sc_game_start_button_unpress.center_y - 200 <= self.mouse_y <= self.sc_game_start_button_unpress.center_y +200 :
                self.is_start_press = True


    def draw_button_screen(self):
        self.sc_game_start_button_unpress = arcade.Sprite("images/start_button.png",1)
        self.sc_game_start_button_unpress.center_x = 600
        self.sc_game_start_button_unpress.center_y = 275
        self.sc_game_start_button_press = arcade.Sprite("images/start_button2.png",1)
        self.sc_game_start_button_press.center_x = 600
        self.sc_game_start_button_press.center_y = 275
        self.is_start_press = False

    def gen_button(self):
        self.buttons = [Button(300,400,self.choices[0]),Button(300,200,self.choices[1]),Button(900,200,self.choices[2]),Button(900,400,self.choices[3])]

    def get_screen(self):
        self.set_screen = Screen(600,350)

    def pause_sound(self):
        self.player.pause()

    def play_sound(self):
        self.player = self.now_song.play()

    def gen_levels(self):
        self.songs_collection.get_songs_and_choices()
