import pygame
import math
from queue import PriorityQueue

WIDTH, HEIGHT = 800, 800
surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* Path Finding Example")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (250, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 220 ,210)

START = "start"
END = "end"
CLOSED = "closed"
OPEN = "open"
WALL = "wall"
KEY = "key"
CHEST = "chest"
PATH = "PATH"
EMPTY = "empty"

STATE_COLORS = {
    START: TURQUOISE,
    END: ORANGE,
    WALL: BLACK,
    EMPTY: WHITE,
    CLOSED: RED,
    OPEN: GREEN,
    PATH: BLUE
}


def h(p1, p2):
    """
    Manhatten distance
    """
    x1, y1 = p1
    x2, y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.change_state(PATH)
        draw()

def astar_algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    
    came_from = {}
    
    g_score = { node: float("inf") for row in grid for node in row }
    g_score[start] = 0

    f_score = { node: float("inf") for row in grid for node in row }
    f_score[start] = h(start.get_pos(), end.get_pos())

    nodes_in_queue = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]

        nodes_in_queue.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())

                if neighbor not in nodes_in_queue:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    nodes_in_queue.add(neighbor)
                    neighbor.change_state(OPEN)

        draw()

        if current != start:
            current.change_state(CLOSED)

    return False

class Node:
    def __init__(self, x, y, width, height, rows, cols):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = WHITE
        self.neighbors = []
        self.rows = rows
        self.cols = cols
        self.state = EMPTY
        self.f = 0
        self.g = 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.get_rect())

    def update_neighbors(self, grid):
        self.neighbors = []

        if self.y < self.rows - 1 and not grid[self.y + 1][self.x].is_wall(): # DOWN
            self.neighbors.append(grid[self.y + 1][self.x])
        
        if self.y > 0 and not grid[self.y - 1][self.x].is_wall(): # UP
            self.neighbors.append(grid[self.y - 1][self.x])
        
        if self.x < self.cols - 1 and not grid[self.y][self.x + 1].is_wall(): # RIGHT
            self.neighbors.append(grid[self.y][self.x + 1])
        
        if self.x > 0 and not grid[self.y][self.x - 1].is_wall(): # LEFT
            self.neighbors.append(grid[self.y][self.x - 1])
        
    def __lt__(self, other):
        return False

    def get_rect(self):
        return (self.x * self.width, self.y * self.height, self.width, self.height)

    def get_pos(self):
        return (self.x * self.width, self.y * self.height)

    def is_closed(self):
        return self.state == CLOSED

    def is_open(self):
        return self.state == OPEN

    def is_wall(self):
        return self.state == WALL

    def is_start(self):
        return self.state == START

    def is_end(self):
        return self.state == END

    def reset(self):
        self.change_state(EMPTY)

    def change_state(self, state):
        self.color = STATE_COLORS[state]
        self.state = state
        pass

def build_grid(rows, cols, width, height):
    grid = []
    node_width = width // cols
    node_height = height // rows

    for y in range(rows):
        grid.append([])
        for x in range(cols):
            node = Node(x, y, node_width, node_height, rows, cols)
            grid[y].append(node)    
    
    return grid

def draw_grid(surface, rows, cols, width, height):
    node_width = width // cols
    node_height = height // rows

    for i in range(rows):
        pygame.draw.line(surface, GREY, (0 , i * node_height), (width, i * node_height))

    for i in range(cols):
        pygame.draw.line(surface, GREY, (i * node_width, 0), (i * node_width, height))

def draw(surface, grid, rows, cols, width, height):
    surface.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(surface)
    
    draw_grid(surface, rows, cols, width, height)
    pygame.display.update()

def get_clicked_pos(pos, rows, cols, width, height):
    node_width = width // cols
    node_height = height // rows
    
    x, y = pos

    col = x // node_width
    row = y // node_height

    return row, col

def main(surface, row_count=50, col_count=50, width=500, height=500):
    grid = build_grid(row_count, col_count, width, height)

    start = None
    end = None
    run = True
    started = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue
            
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, row_count, col_count, width, height)

                node = grid[row][col]

                if not start and node != end: 
                    start = node
                    node.change_state(START)
                elif not end and node != start:
                    end = node
                    node.change_state(END)
                elif node != end and node != start:
                    node.change_state(WALL)
                
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, row_count, col_count, width, height)
                node = grid[row][col]
                node.reset()

                if node == end:
                    end = None
                elif node == start:
                    start = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for rows in grid:
                        for node in rows:
                            node.update_neighbors(grid)

                    astar_algorithm(lambda: draw(surface, grid, row_count, col_count, width, height), grid, start, end)

        draw(surface, grid, row_count, col_count, width, height)
    pygame.quit()
if __name__ == "__main__":
    main(surface, 80, 80, WIDTH, HEIGHT)