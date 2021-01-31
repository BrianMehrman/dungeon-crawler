from lib.entity import Entity
from lib.physics import Physics
from lib.graphics import Graphics

class Actor(Entity):
    def __init__(self, x, y, surface, animation, controller):
        super().__init__(x, y, animation, controller, Physics(self), Graphics(self, animation, surface))
       