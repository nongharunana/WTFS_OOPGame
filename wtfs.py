import arcade
from tkinter import *
from objects import World,Model

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle
    def draw(self):
        self.sync_with_model()
        super().draw()

class WtfsGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.world = World(width, height)
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Life :",self.width - 1100, self.height - 30,arcade.color.WHITE, 20)
        arcade.draw_text(str(self.world.life),self.width - 1025, self.height - 30,arcade.color.WHITE, 20)
        arcade.draw_text("Time : ",self.width - 150, self.height - 30,arcade.color.WHITE, 20)
        arcade.draw_text(str(self.world.time),self.width - 60, self.height - 30,arcade.color.WHITE, 20)
        arcade.draw_text("total songs : ",self.width - 1100, self.height - 670,arcade.color.WHITE, 20)
        arcade.draw_text(str(self.world.score),self.width - 950, self.height - 670,arcade.color.WHITE, 20)


if __name__ == '__main__':
    window = WtfsGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
