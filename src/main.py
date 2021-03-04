
import pygame, os, sys, math, random
import pytmx
from pytmx.util_pygame import load_pygame

from queue import PriorityQueue
from lib.actors.hero import Hero
from lib.animations.animation import Animation, N_ANIM, S_ANIM, E_ANIM, W_ANIM

from lib.controllers.flow_field import FlowField
from lib.world.game_map import GameMap
from lib.systems.ai_system import AiSystem
from lib.systems.graphics_system import GraphicsSystem
from lib.systems.physics_system import PhysicsSystem
from lib.systems.animation_system import AnimationSystem

from lib.views.camera import Camera
from lib.views.world_view import WorldView
from lib.views.hud import Hud

DEBUG_RED = (156, 87, 82)
SCREEN_SIZE = (640, 480)
FPS_CLOCK = pygame.time.Clock()

local_dir = os.path.dirname(__file__)

def local_file(path):
    return os.path.join(local_dir, path)

def load_image(file_name):
    lfile = local_file(file_name)
    print(lfile)
    return pygame.image.load(lfile)

def draw_debug(surface, font, gamedata):
    pos_text = "x={0}  y={1}"
    pos_info = pos_text.format(round(gamedata.rel_x, 2), round(gamedata.rel_y, 2))
    pos_text = font.render(pos_info, True, DEBUG_RED)
    pos_text_rect = pos_text.get_rect(left=16, top=16)
    surface.blit(pos_text, pos_text_rect)
    
    vel_text = "acc={0} vel={1}"
    vel_info = vel_text.format(gamedata.acceleration, gamedata.velocity)
    vel_text = font.render(vel_info, True, DEBUG_RED)
    vel_text_rect = vel_text.get_rect(left=16, top=36)
    surface.blit(vel_text, vel_text_rect)


HALF_WIDTH = SCREEN_SIZE[0] / 2
HALF_HEIGHT = SCREEN_SIZE[1] / 2

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect # l = left,  t = top
    _, _, w, h = camera      # w = width, h = height
    return pygame.Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

def load_player_data(layer):    
    for obj in layer:
        if obj.name == 'Start':
            start_pos = pygame.Vector2(obj.x,obj.y)

    return start_pos

if __name__ == "__main__":
   
    pygame.init()

    surface = pygame.display.set_mode(SCREEN_SIZE)

    font = pygame.font.Font(None, 24)

    last_millis = 0 
    start_pos = None

    # TODO: move the code for loading the character skin to some place else
    hero_animations = {
        N_ANIM: (0,3),
        E_ANIM: (3,3),
        S_ANIM: (6,3),
        W_ANIM: (9,3)
    }
    
    # load entities from map
    # load tiles
    #  -base 
    # - ground
    # - hills ( this layer will have collision)
    # - PlayerData
    map_path = local_file('assets/tilesets/map-01.tmx')

    # TODO: the surfaces should not need to be passed through everywhere. add this to some for of Borg ojbect
    game_map = GameMap(surface, map_path)

    print("Loading hero..")
    hero_img = 'assets/images/rpgsprites1/warrior_f.png'
    hero_animation = Animation(load_image(hero_img), 32, 36, hero_animations, random.randint(0, 1), 0.1)
    
    if game_map.start_pos == None:
        game_map.start_pos = pygame.Vector2(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)

    hero = Hero(game_map.start_pos, surface, hero_animation)

    map_width = game_map.width * game_map.tilewidth
    map_height = game_map.height * game_map.tileheight

    # generate flow field
    flow_pos = pygame.Vector2(0,0)
    flow_size = pygame.Vector2(map_width, map_height)
    flow_field = FlowField(surface, flow_pos, flow_size, game_map)
    
    camera = Camera(simple_camera, map_width, map_height)
    game_map.add_entity(hero)

    aiSystem = AiSystem([entity.controller for entity in game_map.entities if entity.controller])
    animationSystem = AnimationSystem([entity.renderer for entity in game_map.entities if entity.renderer])
    graphicsSystem = GraphicsSystem(surface, [entity.graphics for entity in game_map.entities if entity.graphics], camera)
    physicsSystem = PhysicsSystem([entity.physics for entity in game_map.entities if entity.physics], game_map.collidables)
    
    # Order of this array is important. Entities move, we check collision and move the entities, etc.
    main_systems = [aiSystem, physicsSystem, animationSystem, graphicsSystem]

    # assign hero to camera
    camera_target = hero

    print("Stating game loop.")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        delta_time = last_millis / 1000
        
        camera.update(camera_target.rect)
        
        for control_system in main_systems:
            control_system.update(delta_time)

        flow_field.update(hero, camera)

        draw_debug(surface, font, hero)
        pygame.display.update()

        last_millis = FPS_CLOCK.tick(30)