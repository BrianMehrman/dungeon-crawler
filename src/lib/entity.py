import numpy as np
import pygame


class Entity:
    def __init__(self, x, y, renderer, controller, physics, graphics, colliders=None):
        
        """

        colliders [pygame.Rect] - array of pygame Rects
        TODO:
            * The x and y coordinates of the entity are always in world coordinates. 
            This means to determine where an entity exists on a the grid we must convert the x
            and x coordinates to row and columm coordinates
            * The entity should not need an image, move this to the proper component
        """
        self.x = x
        self.y = y
        self.friction = .12
        self.velocity = pygame.Vector2(0,0)
        self.acceleration = pygame.Vector2(0,0)
        self.controller = controller
        self.renderer = renderer
        self.physics = physics
        self.graphics = graphics
        self.colliders = colliders
        self.timer = 0
        self.direction = (1,0)
        self.move_unit = 32
        self.rel_x = x
        self.rel_y = y

    def get_frame(self):
        return self.renderer.get_frame()

    def get_position(self):
        return (self.rel_x, self.rel_y)

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
        self.renderer.set_direction(self.direction)

    def get_rect(self):
        """
        This rectange is base upon the image rendering. 
        TODO: decouple the graphics from the hit box
        """
        return (self.rel_x, self.rel_y, self.renderer.width, self.renderer.height)

    @property
    def rect(self):
        return pygame.Rect(self.get_rect())

    def get_img(self):
        return self.renderer.img

    def get_width(self):
        return self.renderer.width

    def get_height(self):
        return self.renderer.height