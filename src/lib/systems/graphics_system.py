class GraphicsSystem:
    def __init__(self, surface, components, camera):
        self.components = components
        self.surface = surface
        self.camera = camera
    
    def update(self, delta_time):
        self.surface.fill((0,0,0))
        for component in self.components:
            component.update(delta_time, self.camera)