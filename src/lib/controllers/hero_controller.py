import pygame
import numpy as np

LEFT  = pygame.Vector2(-1,0)
RIGHT = pygame.Vector2(1,0)
UP    = pygame.Vector2(0,-1)
DOWN  = pygame.Vector2(0,1)
ZERO  = pygame.Vector2(0,0)
MAX_X = 2
MAX_Y = 2

class HeroController:
    def __init__(self, entity, speed=1):
        """
        This will attach the users controller to this actor. The last player
        controller actived takes presedence. Like a Freaky Friday mind swap.
        """
        self.entity = entity
        self.timer = 0
        self.speed = speed

    def update(self, delta_time):

        keys = pygame.key.get_pressed()
        self.entity.velocity.xy = pygame.Vector2(0,0)
        new_direction = [0,0]

        if keys[pygame.K_RIGHT]:
            self.entity.velocity += RIGHT
            new_direction[0] = 1
            if self.entity.velocity.x > MAX_X:
                self.entity.velocity.x = MAX_X

        if keys[pygame.K_LEFT]:
            self.entity.velocity += LEFT
            new_direction[0] = -1

            if self.entity.velocity.x < -MAX_X:
                self.entity.velocity.x = -MAX_X

        if keys[pygame.K_UP]:
            self.entity.velocity += UP
            new_direction[1] = -1

            if self.entity.velocity.y < -MAX_Y:
                self.entity.velocity.y = -MAX_Y

        if keys[pygame.K_DOWN]:
            self.entity.velocity += DOWN
            new_direction[1] = 1

            if self.entity.velocity.y > MAX_Y:
                self.entity.velocity.y = MAX_Y

        self.entity.set_direction(new_direction[0],new_direction[1])
