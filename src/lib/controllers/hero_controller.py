import pygame
import numpy as np

ACC_UNIT = 0.3
MIN_VEL = 0.01
MAX_VEL = 1
MIN_ACC = 0.05
MAX_ACC = 0.5
LEFT  = pygame.Vector2(-ACC_UNIT,0)
RIGHT = pygame.Vector2(ACC_UNIT,0)
UP    = pygame.Vector2(0,-ACC_UNIT)
DOWN  = pygame.Vector2(0,ACC_UNIT)

ZERO  = pygame.Vector2(0,0)


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
        
        self.entity.acceleration = pygame.Vector2(0,0)

        new_direction = [0,0]

        if keys[pygame.K_RIGHT]:
            self.entity.acceleration += RIGHT
            new_direction[0] = 1
            
        if keys[pygame.K_LEFT]:
            self.entity.acceleration += LEFT
            new_direction[0] = -1

        if keys[pygame.K_UP]:
            self.entity.acceleration += UP
            new_direction[1] = -1


        if keys[pygame.K_DOWN]:
            self.entity.acceleration += DOWN
            new_direction[1] = 1
    
        self.entity.velocity.x += self.entity.acceleration.x
        self.entity.velocity.y += self.entity.acceleration.y
        
        self.limit_velocity()
        
        if self.entity.acceleration.x == 0:
            self.entity.velocity.x *= .92

        if self.entity.acceleration.y == 0:
            self.entity.velocity.y *= .92

        if new_direction != [0,0]:
            self.entity.set_direction(new_direction[0],new_direction[1])

    def limit_velocity(self):
        self.entity.velocity.x = max(-MAX_VEL, min(self.entity.velocity.x, MAX_VEL))
        self.entity.velocity.y = max(-MAX_VEL, min(self.entity.velocity.y, MAX_VEL))
        
        if abs(self.entity.velocity.x) < MIN_VEL: 
            self.entity.velocity.x = 0
        
        if abs(self.entity.velocity.y) < MIN_VEL: 
            self.entity.velocity.y = 0
   
    def limit_acceleration(self):
        self.entity.acceleration.x = max(-MAX_ACC, min(self.entity.acceleration.x, MAX_ACC))
        self.entity.acceleration.y = max(-MAX_ACC, min(self.entity.acceleration.y, MAX_ACC))
        
        if abs(self.entity.acceleration.x) < MIN_ACC: 
            self.entity.acceleration.x = 0
        
        if abs(self.entity.acceleration.y) < MIN_ACC: 
            self.entity.acceleration.y = 0