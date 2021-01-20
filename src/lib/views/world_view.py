class WorldViewer:
    def __init__(self, actor, world_grid, pos, size, zone_pos, zone_size):
        """
        Takes the world grid data and renders its elements.
        The view is also clamped to the view size.
        The world viewer is also in charge of scrolling the view
        when the observer movers near the 'zone' edge
        Any actor can be give the world viewer, even if it is an NPC.

        actor - The actor the viewer is for. 
        world_grid - Dict of tile entites that make up the world
        pos - tuple of the position on the world grid the viewer is placed
        size - tuple of the width and height of the view
        zone_pos - tuple of the position on the world grid of the zone
        zone_size - tuple of the width and height for the zone
        """
        pass

    def update(self):
        """
        loop through world data and run updates on world objects.
        """

        pass