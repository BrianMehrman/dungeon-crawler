import pygame

class Physics:
    """
    The physics component manages the movement of any entity as well
    as the collision of one object on another.
    """
    def __init__(self, entity, speed=0.25):
        self.entity = entity
        self.speed = speed
        self.timer = 0
        self.collision_tolerance = 10

    def update(self, delta_time, collidables):
        """
        This will do the collision detection
        """
        self.timer += delta_time 

        if self.timer > self.speed:
            self.move(collidables, delta_time)
            
    def move(self, collidables, delta_time):
        self.timer = 0
        x, y, width, height = self.entity.get_rect()

        next_x = x + self.entity.velocity[0] * self.speed * self.entity.move_unit
        next_y = y + self.entity.velocity[1] * self.speed * self.entity.move_unit

        next_rect = pygame.Rect(next_x, next_y, width, height)

        collision_index = next_rect.collidelist(collidables)

        if collision_index > -1:
            collision_rect = collidables[collision_index]
            if abs(next_rect.right - collision_rect.left) < self.collision_tolerance and self.entity.velocity[0] > 0:
                next_x = collision_rect.left - next_rect.width
            
            if abs(next_rect.left - collision_rect.right) < self.collision_tolerance and self.entity.velocity[0] < 0:
                next_x = collision_rect.right

            if abs(next_rect.bottom - collision_rect.top) < self.collision_tolerance and self.entity.velocity[1] > 0:
                next_y = collision_rect.top - next_rect.height

            if abs(next_rect.top - collision_rect.bottom) < self.collision_tolerance and self.entity.velocity[1] < 0:
                next_y = collision_rect.bottom

        self.entity.rel_x = next_x
        self.entity.rel_y = next_y

