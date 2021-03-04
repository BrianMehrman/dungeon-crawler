import pygame
from lib.utils import coord_string

class Node:
    def __init__(self, pos, size, cost=1):
        self.pos = pos
        self.size = size
        self.cost = cost
        self.g = 0
        self.f = 0
        self.dir = None

    def update(self, target):
        self.neighbors = []
        
        grid = self.__cost_nodes

        if self.y < self.rows - 1 and not grid[coord_string(self.y + 1, self.x)].is_blocked(): # DOWN
            self.neighbors.append(grid[coord_string(self.y + 1, self.x)])
        
        if self.y > 0 and not grid[coord_string(self.y - 1, self.x)].is_blocked(): # UP
            self.neighbors.append(grid[coord_string(self.y - 1, self.x)])
        
        if self.x < self.cols - 1 and not grid[coord_string(self.y, self.x + 1)].is_blocked(): # RIGHT
            self.neighbors.append(grid[coord_string(self.y, self.x + 1)])
        
        if self.x > 0 and not grid[coord_string(self.y, self.x - 1)].is_blocked(): # LEFT
            self.neighbors.append(grid[coord_string(self.y, self.x - 1)])


class FlowField:
    # nodes stored by grid coordinates 
    # for example x=1 y=3 '1,3'
    __cost_nodes = {}

    def __init__(self, surface, pos, size, game_map, rez=32):
        """
        pos - x and y position in game world coords
        size - the width and height of the area to create flow field for
        rez - the size of each grid cell.
        """
        self.surface = surface
        self.pos = pos
        self.size = size
        self.rez = rez
        self.game_map = game_map
        self.rows = int(size.y // rez) + 1
        self.cols = int(size.x // rez) + 1
        self.neighbors = []

        print("building flow field")
        for y in range(self.rows):
            for x in range(self.cols):
                # Passing in the dict containing all nodes being created here.
                rect = pygame.Rect(x,y, rez, rez)
                node = Node((x * rez ,y * rez), (rez, rez), self.calculate_cost(rect))
                self.__cost_nodes[coord_string(x,y)] = node

        
        print("flow field complete")


    def update(self, target, camera):
        self.neighbors = []      
        grid = self.__cost_nodes

        for node in self.__cost_nodes.values():
            self.debug_render(node, camera)

    def calculate_cost(self, rect):
        tiles = self.game_map.get_tiles(rect)

        if tiles:
            return sum([tile.cost for tile in tiles])

        return 1 

    def debug_render(self, node, camera):
        # Initialing Color 
        color = (255,0,0) 
        
        # Drawing Rectangle 
        pygame.draw.rect(self.surface, color, camera.apply(pygame.Rect(node.pos, node.size)),  2) 

if __name__ == "__main__":
    field =  FlowField()

    field.update()