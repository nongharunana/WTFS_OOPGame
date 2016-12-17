import arcade

class Botton:
    def __init__(self,x,y,text):
        self.center_x = x
        self.center_y = y
        self.image_press = arcade.Sprite("images/bot2.png",1)
        self.image_press.center_x = self.center_x
        self.image_press.center_y = self.center_y
        self.image_unpress = arcade.Sprite("images/bot1.png",1)
        self.image_unpress.center_y = self.center_y
        self.image_unpress.center_x = self.center_x
        self.text = text
        self.mouse_on = False

class Screen:
    def __init__(self,x,y):
        self.sc_center_x = x
        self.sc_center_y = y
        self.sc_gameover = arcade.Sprite("images/gameover.png",1)
        self.sc_gameover.center_x = self.sc_center_x
        self.sc_gameover.center_y = self.sc_center_y
        self.sc_game_start = arcade.Sprite("images/start.png",1)
        self.sc_game_start.sc_center_x = self.sc_center_x
        self.sc_game_start.sc_center_y = self.sc_center_y
        self.sc_play = arcade.Sprite("images/play.png",1)
        self.sc_play.center_x = self.sc_center_x
        self.sc_play.center_y = self.sc_center_y
