import pygame, os, sys
import random
from pygame.locals import *

pygame.init()

local_dir = os.path.dirname(__file__)

fps_clock = pygame.time.Clock()
surface = pygame.display.set_mode((640, 480))
font = pygame.font.Font(None, 32)
moves = {
    0: (0,1),
    1: (-1, 0),
    2: (0, -1),
    3: (0, 1) 
}
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class GameData():
    def __init__(self):
        self.lives = 3
        self.is_dead = False
        self.blocks = []
        self.tick = 250
        self.speed = 250
        self.level = 1
        self.berrycount = 0
        self.segments = 1
        self.frame = 0

        bx = random.randint(1, 38)
        by = random.randint(1, 28)

        self.berry = Position(bx, by)
        self.blocks.append(Position(20, 15))
        self.blocks.append(Position(19, 15))
        self.direction = 0

def lose_life(gamedata):
    gamedata.lives -= 1
    gamedata.direction = 0
    gamedata.blocks[:] = []
    gamedata.blocks.append(Position(20,15))
    gamedata.blocks.append(Position(19,15))

def local_file(path):
    return os.path.join(local_dir, path)

def position_berry(gamedata):
    bx = random.randint(1, 38)
    by = random.randint(1, 28)

    found = True

    while (found):
        found = False
        for b in gamedata.blocks:
            if (b.x == bx and b.y == by):
                found = True

        if (found):
            bx = random.randint(1, 38)
            by = random.randint(1, 28)

    gamedata.berry = Position(bx, by)

def load_map_file(file_name):
    f = open(local_file(file_name), 'r')
    content = f.readlines()
    f.close()
    return content

def head_hit_body(gamedata):
    head = gamedata.blocks[0]

    for b in gamedata.blocks:
        if (b != head) and (b.x == head.x and b.y == head.y):
            return True
    return False

def head_hit_wall(map, gamedata):
    row = 0
    for line in map:
        col = 0
        for char in line:
            if (char == '1') and (gamedata.blocks[0].x == col and gamedata.blocks[0].y == row):
                return True
            col += 1
        row += 1

    return False

def draw_data(surface, gamedata):
    text = "Lives = {0}, Level = {1}"
    info = text.format(gamedata.lives, gamedata.level)
    text = font.render(info, 0, (255,255,255))
    textpos = text.get_rect(centerx=surface.get_width()/2, top=32)
    surface.blit(text, textpos)

def draw_game_over(surface):
    surface.fill((0, 0, 0))
    text1 = font.render("Game Over", 1, (255, 255, 255))
    text2 = font.render("Space to play or close the window", 1, (255, 255, 255))

    cx = surface.get_width() / 2
    cy = surface.get_height() / 2

    textpos1 = text1.get_rect(centerx=cx, top=cy - 48)
    textpos2 = text2.get_rect(centerx=cx, top=cy)

    surface.blit(text1, textpos1)
    surface.blit(text2, textpos2)


def draw_walls(surface, img, snakemap):
    row = 0
    img_width = 16
    img_height = 16

    for line in snakemap:
        col = 0
        for char in line:
            if (char == '1'):
                img_rect = img.get_rect()
                img_rect.left = col * img_width
                img_rect.top = row * img_height
                surface.blit(img, img_rect)
            col += 1

        row += 1

def draw_snake(surface, img, gamedata):
    first = True

    for b in gamedata.blocks:
        dest = (b.x * 16, b.y * 16, 16, 16)

        # first head direction and animation frame
        if first:
            first = False
            src = (((gamedata.direction * 2) + gamedata.frame) * 16, 0, 16, 16)
        else:
            src = (8 * 16, 0, 16, 16)

        surface.blit(img, dest, src)

def update_game(gamedata, gametime):
    gamedata.tick -= gametime
    head = gamedata.blocks[0]

    if (gamedata.tick < 0):
        gamedata.tick += gamedata.speed
        gamedata.frame += 1
        gamedata.frame %= 2

        if (gamedata.direction == 0):
            move = (1, 0)
        elif (gamedata.direction == 1):
            move = (-1, 0)
        elif (gamedata.direction == 2):
            move = (0, -1)
        else:
            move = (0, 1)        
        
        newpos = Position(head.x + move[0], head.y + move[1])

        first = True

        for b in gamedata.blocks:
            temp = Position(b.x, b.y)
            b.x = newpos.x
            b.y = newpos.y
            newpos = Position(temp.x, temp.y)

    keys = pygame.key.get_pressed()

    if (keys[K_RIGHT] and gamedata.direction != 1):
        gamedata.direction = 0
    elif (keys[K_LEFT] and gamedata.direction != 0):
        gamedata.direction = 1
    elif (keys[K_UP] and gamedata.direction != 3):
        gamedata.direction = 2
    elif (keys[K_DOWN] and gamedata.direction != 2):
        gamedata.direction = 3

    if (head.x == gamedata.berry.x and head.y == gamedata.berry.y):
        last = len(gamedata.blocks) - 1
        for i in range(gamedata.segments):
            blockX = gamedata.blocks[last].x
            blockY = gamedata.blocks[last].y
            gamedata.blocks.append(Position(blockX, blockY))

        bx = random.randint(1, 38)
        by = random.randint(1, 28)
        gamedata.berry = Position(bx, by)
        gamedata.berrycount += 1

        if (gamedata.berrycount == 10):
            gamedata.berrycount = 0
            gamedata.speed -= 25
            gamedata.level += 1
            gamedata.segments *= 2

            if (gamedata.segments > 64):
                gamedata.segments = 64
            
            if (gamedata.speed < 100):
                gamedata.speed = 100

def load_image(file_name):
    return pygame.image.load(local_file(file_name))

def load_images():
    wall = load_image('wall.png')
    raspberry = load_image('berry.png')
    snake = load_image('snake.png')
    return { 'wall': wall, 'berry': raspberry, 'snake': snake }


images = load_images()
images['berry'].set_colorkey((255, 0 , 255))

snakemap = load_map_file('map.txt')

data = GameData()
quit_game = False
is_playing = False

while not quit_game:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if is_playing:
        x = random.randint(1, 38)
        y = random.randint(1, 28)

        rrect = images['berry'].get_rect()
        rrect.left = data.berry.x * 16
        rrect.top = data.berry.y * 16

        # Do update stuff here
        update_game(data, fps_clock.get_time())

        crashed = head_hit_wall(snakemap, data) or head_hit_body(data)

        if crashed:
            lose_life(data)
            position_berry(data)

        is_playing = (data.lives > 0)
        if is_playing:
            surface.fill((0, 0, 0))
            # Do drawing stuff here
            draw_walls(surface, images['wall'], snakemap)
            surface.blit(images['berry'], rrect)
            draw_snake(surface, images['snake'], data)

            draw_data(surface, data)
    else:
        keys = pygame.key.get_pressed()

        if (keys[K_SPACE]):
            is_playing = True
            data = None
            data = GameData()

        draw_game_over(surface)
    
    pygame.display.update()
    fps_clock.tick(30)
