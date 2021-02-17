import pygame
import numpy as np

ACC_UNIT = 0.3
MIN_VEL = 0.01
MAX_VEL = 3
MIN_ACC = 0.05
MAX_ACC = 0.5
LEFT  = pygame.Vector2(-ACC_UNIT,0)
RIGHT = pygame.Vector2(ACC_UNIT,0)
UP    = pygame.Vector2(0,-ACC_UNIT)
DOWN  = pygame.Vector2(0,ACC_UNIT)

ZERO  = pygame.Vector2(0,0)


class HeroController:
    def __init__(self, entity, speed=0.1):
        """
        This will attach the users controller to this actor. The last player
        controller actived takes presedence. Like a Freaky Friday mind swap.
        """
        self.entity = entity
        self.timer = 0
        self.speed = speed

    def update(self, delta_time):

        keys = pygame.key.get_pressed()
        
        # if the user stops holding buttons the user stops
        new_direction = [0,0]

        if keys[pygame.K_RIGHT]:
            new_direction[0] = 1
            
        if keys[pygame.K_LEFT]:
            new_direction[0] = -1

        if keys[pygame.K_UP]:
            new_direction[1] = -1

        if keys[pygame.K_DOWN]:
            new_direction[1] = 1
    
        self.entity.set_direction(new_direction[0],new_direction[1])



    