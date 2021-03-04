
import pygame, os
import pytmx
from pytmx.util_pygame import load_pygame
from lib.animations.static import Static
from lib.world.tile import Tile
from lib.utils import coord_string



def load_map_data(file_path):
    return load_pygame(file_path)

def load_player_data(layer):    
    for obj in layer:
        if obj.name == 'Start':
            start_pos = pygame.Vector2(obj.x,obj.y)

    return start_pos

class GameMap:
    def __init__(self, surface, map_path):
        self.surface = surface
        self.tiled_map_data = load_map_data(map_path)
        self.tiles = {}
        self.entities = []
        self.collidables = []
        self.start_pos = None
        self.load_layers()

    @property
    def height(self):
        return self.tiled_map_data.height

    @property
    def width(self):
        return self.tiled_map_data.width

    @property
    def tileheight(self):
        return self.tiled_map_data.tileheight

    @property
    def tilewidth(self):
        return self.tiled_map_data.tilewidth

    def add_entity(self, entity):
        if entity not in self.entities:
            self.entities.append(entity)

    def get_tiles(self, rect):
        """
        returns array of the tiles the intersect with rect
        """        
        tiles = list(self.tiles.values())
        tile_rects = [tile.get_rect() for tile in tiles]

        # order is important
        collide_list = rect.collidelistall(tile_rects)

        if collide_list:
            return [tiles[i] for i in collide_list]

        return []

    def load_layers(self):
        for layer in self.tiled_map_data.layers:

            print("Loading layer %s..." % layer.name)

            if isinstance(layer, pytmx.TiledTileLayer):
               self.load_tiles(layer)

            if layer.name == 'PlayerData':
                self.start_pos = load_player_data(layer)
            
            print("---")

    def load_tiles(self, layer):
        
        print("loading tiles...")
        for x, y, gid in layer:
            image = layer.parent.images[gid]
            colliders = []
            
            if image is None:
                continue

            world_x, world_y = x * image.get_width(), y * image.get_height()
            
            static_renderer = Static(image, 0, 0, image.get_width(), image.get_height())
            props = self.tiled_map_data.get_tile_properties_by_gid(gid)

            if 'colliders' in props:
                for raw in props['colliders']:
                    self.collidables.append(pygame.Rect(world_x + raw.x, world_y + raw.y, raw.width, raw.height))

            tile = Tile(world_x, world_y, self.surface, static_renderer, colliders)

            self.tiles[coord_string(x,y)] = tile
            self.entities.append(tile)
    
