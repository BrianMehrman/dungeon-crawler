import pygame

ACC_UNIT = 0.3
MIN_VEL = 0.01
MAX_VEL = 3
MIN_ACC = 0.05
MAX_ACC = 0.5
FRICTION = 0.72

LEFT  = pygame.Vector2(-ACC_UNIT,0)
RIGHT = pygame.Vector2(ACC_UNIT,0)
UP    = pygame.Vector2(0,-ACC_UNIT)
DOWN  = pygame.Vector2(0,ACC_UNIT)

class Physics:
    """
    The physics component manages the movement of any entity as well
    as the collision of one object on another.
    """
    def __init__(self, entity, speed=0.05):
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

        if self.entity.direction[0] == 1:
            self.entity.acceleration += RIGHT
        elif self.entity.direction[0] == -1:
            self.entity.acceleration += LEFT
        else:
            self.entity.acceleration[0] = 0

        if self.entity.direction[1] == 1:
            self.entity.acceleration += DOWN
        elif self.entity.direction[1] == -1:
            self.entity.acceleration += UP
        else:
            self.entity.acceleration[1] = 0

        self.limit_acceleration()

        self.entity.velocity.x += self.entity.acceleration.x
        self.entity.velocity.y += self.entity.acceleration.y
        
        if self.entity.acceleration.x == 0:
            self.entity.velocity.x *= FRICTION

        if self.entity.acceleration.y == 0:
            self.entity.velocity.y *= FRICTION

        self.limit_velocity()

        # get next position point
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