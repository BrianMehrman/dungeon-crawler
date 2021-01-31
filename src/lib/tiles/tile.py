from lib.entity import Entity
from lib.physics import Physics
from lib.graphics import Graphics

class Tile(Entity):
    def __init__(self, x, y, surface, renderer, colliders):
        super().__init__(x, y, renderer, None, None, Graphics(self, renderer, surface), colliders)