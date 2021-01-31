import pygame

class Graphics:
    def __init__(self, entity, renderer, surface, speed=0.1):
        self.entity = entity
        self.width = renderer.width
        self.surface = surface
        self.speed = speed
        self.timer = 0

    def update(self, delta_time, camera):
        """
        renders the graphics for an entity on a surface.
        since we controll the enties ability to draw we controll the redraw 
        """
        self.timer += delta_time
        # redraw
        if self.timer > self.speed:
            self.timer = 0
            # pygame.draw.rect(self.surface, (255, 0, 0), self.entity.get_rect())
        
        self.surface.blit(self.entity.get_img(), camera.apply(self.entity), self.entity.renderer.get_rect())