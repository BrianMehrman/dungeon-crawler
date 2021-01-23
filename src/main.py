
import pygame, os, sys, math, random

from queue import PriorityQueue
from lib.actors.hero import Hero
from lib.animations.animation import Animation, N_ANIM, S_ANIM, E_ANIM, W_ANIM

from lib.systems.ai_system import AiSystem
from lib.systems.graphics_system import GraphicsSystem
from lib.systems.physics_system import PhysicsSystem
from lib.systems.animation_system import AnimationSystem

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
   
    pygame.init()

    surface = pygame.display.set_mode(SCREEN_SIZE)
    last_millis = 0 

    # sx = -50 + random.random() * 100
    # sy = -50 + random.random() * 100
    entities = []

    # TODO: move the code for loading the character skin to some place else
    hero_animations = {
        N_ANIM: (0,3),
        E_ANIM: (3,3),
        S_ANIM: (6,3),
        W_ANIM: (9,3)
    }

    hero_img = 'assets/images/rpgsprites1/warrior_f.png'
    hero_animation = Animation(load_image(hero_img), 32, 36, hero_animations, random.randint(0, 1), 0.25)
    hero  = Hero(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2, surface, hero_animation)

    entities.append(hero)

    aiSystem = AiSystem([entity.controller for entity in entities])
    animationSystem = AnimationSystem([entity.animation for entity in entities])
    graphicsSystem = GraphicsSystem(surface, [entity.graphics for entity in entities])
    physicsSystem = PhysicsSystem([entity.physics for entity in entities])

    # Order of this array is important. Entities move, we check collision and move the entities, etc.
    main_systems = [aiSystem, physicsSystem, animationSystem, graphicsSystem]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        delta_time = last_millis / 1000

        for control_system in main_systems:
            control_system.update(delta_time)
       
        pygame.display.update()

        last_millis = FPS_CLOCK.tick(30)