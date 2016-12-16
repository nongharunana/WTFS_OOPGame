import arcade

class Botton:
    def __init__(self,x,y,text):
        self.center_x = x
        self.center_y = y
        self.image_press = arcade.Sprite("images/bot2.png",1)
        self.image_press.center_x = self.center_x
        self.image_press.center_y = self.center_y
        self.image_unpress = arcade.Sprite("images/bot1.png",2)
        self.image_unpress.center_y = self.center_y
        self.image_unpress.center_x = self.center_x
        self.text = text
