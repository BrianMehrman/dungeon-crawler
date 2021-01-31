import pygame

class WorldView:
    def __init__(self, actor, zone_pos, zone_size, tiles, tile_size):
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
        self.actor = actor
        self.tiles = tiles
        self.zone_pos = zone_pos
        self.zone_size = zone_size

    def update(self):
        """
        loop through world data and run updates on world objects.
        """

        self.move()
        for tile in self.tiles:
            tile.rel_x = tile.x - self.zone_pos[0]
            tile.rel_y = tile.y - self.zone_pos[1] 

            for collider in tile.colliders:
                collider.rel_x = collider.x - self.zone_pos[0]
                collider.rel_y = collider.y - self.zone_pos[1]


    def move(self):
        actor_rect = pygame.Rect(self.actor.get_rect())
        tile_edge = actor_rect.width * 2
        
        if abs(actor_rect.left - self.zone_pos[0]) <= tile_edge:
            self.zone_pos[0] -= tile_edge
        if abs(actor_rect.right - (self.zone_pos[0] + self.zone_size[0])) <= tile_edge:
            self.zone_pos[0] += tile_edge

        if abs(actor_rect.top - self.zone_pos[1]) <= tile_edge:
            self.zone_pos[0] -= tile_edge
        if abs(actor_rect.bottom - (self.zone_pos[1] + self.zone_size[1])) <= tile_edge:
            self.zone_pos[0] += tile_edge
