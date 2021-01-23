from lib.controllers.npc_controller import NpcController
class Npc(Actor):
    def __init__(self, x, y, surface, animation):
        super().__init__(x, y, surface, animation, NpcController(self))
