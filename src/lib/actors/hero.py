from lib.actors.actor import Actor
from lib.controllers.hero_controller import HeroController

class Hero(Actor):
    def __init__(self, pos, surface, animation):
        super().__init__(pos.x, pos.y, surface, animation, HeroController(self))
