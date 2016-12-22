import arcade
from objects import World
from model_default import Model
from botton import Screen

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

class WtfsGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.world = World(width, height)

    def animate(self,delta):
        self.world.mouse_detect_start_button()
        self.world.status_screen()
        if self.world.status_game == self.world.status_play:
            self.world.animate(delta)


    def on_draw(self):
        arcade.start_render()
        self.draw_screen()
        self.draw_text()
        self.draw_botton()

    def draw_botton(self):
        if self.world.status_game == self.world.status_play:
            for botton in self.world.bottons:
                if botton.mouse_on:
                    botton.image_press.draw()
                else:
                    botton.image_unpress.draw()
                arcade.draw_text(botton.text,botton.center_x,botton.center_y,arcade.color.BLACK,20,align = "center",anchor_x = "center" , anchor_y ="center")
        if self.world.status_game == self.world.status_start:
            if self.world.is_start_press :
                self.world.sc_game_start_button_press.draw()
            else :
                self.world.sc_game_start_button_unpress.draw()


    def draw_screen(self):
        if self.world.status_game == self.world.status_start:
                self.world.set_screen.sc_game_start.draw()
        if self.world.status_game == self.world.status_gameover:
                self.world.set_screen.sc_gameover.draw()

    def draw_text(self):
        if self.world.status_game == self.world.status_play:
            arcade.draw_text("WTFS",self.width - 750 ,self.height - 150,arcade.color.WHITE,100)
        if self.world.status_game == self.world.status_gameover:
            arcade.draw_text(str(self.world.score),self.width - 620, self.height - 480,arcade.color.RED, 100)

    def on_mouse_press(self,x,y,button,modifiers):
        self.world.is_press = True

    def on_mouse_motion(self,x,y,dx,dy):
        self.world.mouse_x = x
        self.world.mouse_y = y

if __name__ == '__main__':
    window = WtfsGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
