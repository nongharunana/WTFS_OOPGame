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
        self.songs_name.append("closer")
        self.songs_name.append("come back to me")
        self.songs_name.append("counting stars")
        self.songs_name.append("don't let me down")
        self.songs_name.append("faded")
        self.songs_name.append("lean on")
        self.songs_name.append("love me like you do")
        self.songs_name.append("one call away")
        self.songs_name.append("pretty boy")
        self.songs_name.append("sugar")
        self.songs_name.append("thinking out loud")
        self.songs_name.append("we don't talk anymore")
        self.songs_name.append("work from home")
        self.songs_name.append("กลับตัวกลับใจ")
        self.songs_name.append("เจ็บที่ยังรู้สึก")
        self.songs_name.append("ฉันมาบอกว่า")
        self.songs_name.append("ทางของฝุ่น")
        self.songs_name.append("เธอมีฉัน ฉันมีใคร")
        self.songs_name.append("ไม่รักเธอ")
        self.songs_name.append("รักต้องเปิด")
        self.songs_name.append("เรื่องที่ขอ")
        self.songs_name.append("วันหนึ่ง")
        self.songs_name.append("วายร้าย")
        self.songs_name.append("สักวันคงได้พบกัน")
        self.songs_name.append("สิ่งของ")
        self.songs_name.append("หัวใจคนรอ")
        self.songs_name.append("อย่าทำให้ฉันคิด")
        self.songs_name.append("อ้าว")
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
        index = 0
        rand_index=[]
        while len(rand_index) < 4:
            i = randint(0,3)
            if not i in rand_index :
                rand_index.append(i)
        choices_new=[]
        i = randint(0,len(self.songs_sound)-1)
        self.world.now_song = self.songs_sound[i]
        self.world.true_song = self.songs_name[i]
        choices = [self.songs_name[i]]
        while len(choices) < 4 :
            i = randint(0,len(self.songs_sound)-1)
            if not self.songs_name[i] in choices :
                choices.append(self.songs_name[i])
        while index < 4:
            choices_new.append(choices[rand_index[index]])
            index += 1
        self.world.choices = choices_new
