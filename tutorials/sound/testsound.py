import pygame, os, sys
from utils import local_file
pygame.mixer.init()

shootSound = pygame.mixer.Sound(local_file('playershoot.wav'))

shootSound.play()

while pygame.mixer.get_busy():
    pass

pygame.mixer.quit()
