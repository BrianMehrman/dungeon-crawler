from lib.navigation import NORTH, SOUTH, EAST, WEST
import pygame as pg
import math


class Static:
    def __init__(self, img, x, y, width, height):
        """
        This class must have a sprite sheet with at least one animation
        Args:
            img: pygame.image of the sprite sheet
            animations: dict of animation tuples containing an offset and length, using animation names as the keys
            frame: current frame of animation to be on
            clip_lenght: the lenght of the animation
            speed: the speed at which the animation should run.
        """
        self.x = x
        self.y = y 
        self.img = img
        self.width = width
        self.height = height
        self.timer = 0
        self.direction = (1,0)

    def get_rect(self):
        return pg.Rect(self.get_x(), self.get_y(), self.width, self.height)

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def update(self, delta_time):
        """
        static graphics have nothing to update ATM
        """
        pass