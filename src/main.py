
import pygame, os, sys, math

from queue import PriorityQueue
from lib.actors.hero import Hero
from lib.animations.animation import Animation
SCREEN_SIZE = (640, 480)
FPS_CLOCK = pygame.time.Clock()


local_dir = os.path.dirname(__file__)

def local_file(path):
    return os.path.join(local_dir, path)

def load_image(file_name):
    lfile = local_file(file_name)
    print(lfile)
    return pygame.image.load(lfile)

if __name__ == "__main__":
   
    """
    Actor
    - controller component
    -- AI (finite state machine)
    -- User controller
    
    Actor -> Hero
    Actor -> Enemy

    """

    """
    Game Play

    - Actions
    -- Use/Item
    -- Attack
    -- Walk
    -- LOS
    -- Toss /Throw

    """

    """
    Item System

    - Items
    -- consumable
    -- durable/multi-use
    - Weapons
    -- short range
    -- long range (use toss action)
    -- magic??
    - Armor
    --

    """

    """
    game loops

    -- animation
    -- movement
    -- player controls
    -- attacks
    -- physics
    -- rendering

    """

    pygame.init()

    surface = pygame.display.set_mode(SCREEN_SIZE)
    last_millis = 0 

    sx = -50 + random.random() * 100
    sy = -50 + random.random() * 100
    entities = []
    hero_animation = Animation(local_file('src/assets/images/cloakandleather.png'), random.randint(0, 1), 2, (sx, sy))
    
    hero  = Hero(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2, hero_animation)

    entities.append(hero)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        delta_time = last_millis / 1000

        for entity in entities:
            entity.update(delta_time)

        surface.fill((0, 0, 0))

        for entity in entities:
            entity.draw(surface)

        pygame.display.update()

        last_millis = fps_clock.tick(30)