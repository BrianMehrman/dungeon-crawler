from lib.actors.actor import Actor
from lib.controllers.hero_controller import HeroController

class Hero(Actor):
    def __init__(self, x, y, surface, animation):
        super().__init__(x, y, surface, animation, HeroController(self))
