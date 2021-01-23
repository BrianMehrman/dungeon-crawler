class PhysicsSystem:
    def __init__(self, components):
        self.components = components
    
    def update(self, delta_time):
        for component in self.components:
            component.update(delta_time)