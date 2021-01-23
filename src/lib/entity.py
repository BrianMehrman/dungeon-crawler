import numpy as np
import pygame


class Entity:
    def __init__(self, x, y, animation, controller, physics, graphics):
        
        """
        TODO:
            * The x and y coordinates of the entity are always in world coordinates. 
            This means to determine where an entity exists on a the grid we must convert the x
            and x coordinates to row and columm coordinates
            * The entity should not need an image, move this to the proper component
        """
        self.x = x
        self.y = y
        self.velocity = pygame.Vector2(0,0)
        self.controller = controller
        self.animation = animation
        self.physics = physics
        self.graphics = graphics
        self.timer = 0
        self.direction = (1,0)
        self.move_unit = 32

    def get_frame(self):
        return self.animation.get_frame()

    def get_position(self):
        return (self.x, self.y)

    def get_direction(self):
        """
        finds a normalized direction vector from the velocity.
        """
        return self.direction
    
    def set_direction(self, x=None, y=None):
        if x is None:
            new_x = self.direction[0]
        else:
            new_x = x 

        if y is None:
            new_y = self.direction[1]
        else:
            new_y = y

        if new_y == 0 and new_x == 0:
            # there is no idle anim yet
            new_x = 1

        self.direction = (new_x, new_y)

        # TODO: having to maintain the direction in two places needs to be fixed
        self.animation.set_direction(self.direction)

    def get_rect(self):
        return (self.x, self.y, self.animation.width, self.animation.height)

    def get_img(self):
        return self.animation.img

    def get_width(self):
        return self.animation.width

    def get_height(self):
        return self.animation.height