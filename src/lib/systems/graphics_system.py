class GraphicsSystem:
    def __init__(self, surface, components):
        self.components = components
        self.surface = surface
    
    def update(self, delta_time):
        self.surface.fill((0,0,0))
        for component in self.components:
            component.update(delta_time)