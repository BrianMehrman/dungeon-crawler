
class Entity:
    def __init__(self, x, y, animation, controller, physics, graphics):
        self.x = x
        self.y = y
        self.controller = controller
        self.animation = animation
        self.physics = physics
        self.graphics = graphics
        self.timer = 0

    def update(self, delta_time):
        """
        This will update the actor, override this method in the subclass.
        """
        
        self.timer += delta_time

        # update animation
        if self.timer >= self.animation.speed:
            self.animation.next_frame()

        # update ai / controller


        # update physics / bounding box

        # update graphics