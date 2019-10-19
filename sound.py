import pygame
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
exit_sound = pygame.mixer.Sound(file="Sounds\exit_sound.wav")

exit_sound.play()

while True:
    pass