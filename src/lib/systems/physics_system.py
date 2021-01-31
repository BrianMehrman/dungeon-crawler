class PhysicsSystem:
    def __init__(self, components, collidables):
        self.components = components
        self.collidables = collidables
    
    def update(self, delta_time):
        for component in self.components:
            component.update(delta_time, self.collidables)