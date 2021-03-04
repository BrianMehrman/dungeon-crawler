import pygame

class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)
        
    def apply(self, rect):
        return rect.move(self.state.topleft)
        
    def update(self, rect):
        self.state = self.camera_func(self.state, rect)