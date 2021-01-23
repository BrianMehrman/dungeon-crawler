class Physics:
    """
    The physics component manages the movement of any entity as well
    as the collision of one object on another.
    """
    def __init__(self, entity, speed=0.25):
        self.entity = entity
        self.speed = speed
        self.timer = 0

    def update(self, delta_time):
        """
        This will do the collision detection
        """
        self.timer += delta_time 

        if self.timer > self.speed:
            self.move()
            
    def move(self):
        self.timer = 0
        self.entity.x += self.entity.velocity[0] * self.speed * self.entity.move_unit
        self.entity.y += self.entity.velocity[1] * self.speed * self.entity.move_unit
