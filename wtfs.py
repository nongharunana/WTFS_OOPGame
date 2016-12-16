import arcade
from objects import World
from model_default import Model

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

class WtfsGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
        self.world = World(width, height)

    def animate(self,delta):
        self.world.animate(delta)

    def on_draw(self):
        arcade.start_render()
        self.draw_text()
        self.draw_botton()

    def draw_botton(self):
        for botton in self.world.bottons:
            if botton.mouse_on:
                botton.image_press.draw()
            else:
                botton.image_unpress.draw()
            arcade.draw_text(botton.text,botton.center_x,botton.center_y,arcade.color.BLACK,20,align = "center",anchor_x = "center" , anchor_y ="center")


    def draw_text(self):
        arcade.draw_text("Life :",self.width - 1100, self.height - 30,arcade.color.WHITE, 20)
        arcade.draw_text(str(self.world.life),self.width - 1025, self.height - 30,arcade.color.WHITE, 20)
        #arcade.draw_text("Time : ",self.width - 150, self.height - 30,arcade.color.WHITE, 20)
        #arcade.draw_text(str(self.world.time),self.width - 60, self.height - 30,arcade.color.WHITE, 20)
        arcade.draw_text("total songs : ",self.width - 1100, self.height - 670,arcade.color.WHITE, 20)
        arcade.draw_text(str(self.world.score),self.width - 950, self.height - 670,arcade.color.WHITE, 20)

    def on_mouse_press(self,x,y,button,modifiers):
        self.world.is_press = True

    def on_mouse_motion(self,x,y,dx,dy):
        self.world.mouse_x = x
        self.world.mouse_y = y

if __name__ == '__main__':
    window = WtfsGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
