from lib.entity import Entity

class Actor(Entity):
    def __init__(self, x, y, animation, controller, pyhsics, graphics):
        super(x, y, animation, controller, physics, graphics)
        
        self.speed = speed

    def draw(self, surface):
        """
        This method will render the actor on the surface. All actors show have an 
        object that we can call to render. 

        hmmm, not sure what to call this
        """
        self.renderer.draw()