import pygame
from utils import load_image, local_file
from models.robot import Robot

class RobotView(object):
    def __init__(self, img_path):
        self.img = load_image(img_path)
        self.img.set_colorkey((0, 0, 0))

    def draw(self, surface, models):
        for model in models:
            rect = pygame.Rect(model.get_frame() * 32, 0, 32, 32)
            surface.blit(self.img, model.get_position(), rect)