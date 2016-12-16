import arcade
import arcade.sound
from random import randint,random

class SongsCollection:
    def __init__(self,world):
        self.songs_name = []
        self.songs_sound = []
        self.songs_name.append("baby")
        self.songs_name.append("let it go")
        self.songs_name.append("my heart will go on")
        self.songs_name.append("ขัดใจ")
        self.songs_name.append("ยาพิษ")
        self.loading_songs(self.songs_name)
        self.world = world

    def loading_songs(self,names):
        for name in names :
            new_name = ""
            for i in name :
                if i != ' ':
                    new_name += i
                else:
                    new_name += '_'

            fullpath = "songs/"+new_name+".mp3"
            self.songs_sound.append(arcade.sound.load_sound(fullpath))

    def get_songs_and_choices(self):
        i = randint(0,len(self.songs_sound)-1)
        self.world.now_song = self.songs_sound[i]
        self.world.true_song = self.songs_name[i]
        choices = [self.songs_name[i]]
        while len(choices) < 4 :
            i = randint(0,len(self.songs_sound)-1)
            if not self.songs_name[i] in choices :
                choices.append(self.songs_name[i])

        self.world.choices = choices
