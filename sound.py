#Pygame is used only to play sounds in this game.
from pygame import mixer
#mixer.pre_init(44100, 16, 2, 4096)
mixer.init()
exit_sound = mixer.Sound(file="Sounds\exit_sound.wav")
pickup_sound = mixer.Sound(file="Sounds\Drop.wav")
mixer.music.load("Sounds\BG_Music.wav")

def play_exit_sound():
    if not mixer.get_busy():
        exit_sound.play()

def play_pickup_sound():
    if not mixer.get_busy():
        pickup_sound.play()

def BG_Music(play = True):
    if play:
        if not mixer.music.get_busy():
            mixer.music.play(-1)
    else:
        mixer.music.stop()
