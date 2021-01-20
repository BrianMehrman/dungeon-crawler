import pygame
from models.robot import Robot
from utils import load_image
class RadarView(object):

    def __init__(self, blip_img_path, border_img_path):
        self.blip_image = load_image(blip_img_path)
        self.border_image = load_image(border_img_path)

    def draw(self, surface, robots):
        for robot in robots:
            x, y = robot.get_position()
            x /= 10
            y /= 10

            x += 1
            y += 1

            surface.blit(self.blip_image, (x, y))

        surface.blit(self.border_image, (0, 0))