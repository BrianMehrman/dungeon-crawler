
import pygame, os, sys, math, random
import pytmx
from pytmx.util_pygame import load_pygame

from queue import PriorityQueue
from lib.actors.hero import Hero
from lib.tiles.tile import Tile
from lib.animations.animation import Animation, N_ANIM, S_ANIM, E_ANIM, W_ANIM
from lib.animations.static import Static

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

def load_map(file_path):
    return load_pygame(local_file(file_path))

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

def load_tiles(layer):
    collidables = []
    entities = []

    print("loading tiles...")
    for x, y, gid in layer:
        image = layer.parent.images[gid]
        colliders = []
        
        if image is None:
            continue

        world_x, world_y = x * image.get_width(), y * image.get_height()
        
        static_renderer = Static(image, 0, 0, image.get_width(), image.get_height())
        props = tiled_map.get_tile_properties_by_gid(gid)

        if 'colliders' in props:
            for raw in props['colliders']:
                collidables.append(pygame.Rect(world_x + raw.x, world_y + raw.y, raw.width, raw.height))

        tile = Tile(world_x, world_y, surface, static_renderer, colliders)
        
        if colliders:
            collidables.append(tile)

        entities.append(tile)
    
    return entities, collidables

if __name__ == "__main__":
   
    pygame.init()

    surface = pygame.display.set_mode(SCREEN_SIZE)

    font = pygame.font.Font(None, 24)

    last_millis = 0 
    entities = []

    # TODO: move the code for loading the character skin to some place else
    hero_animations = {
        N_ANIM: (0,3),
        E_ANIM: (3,3),
        S_ANIM: (6,3),
        W_ANIM: (9,3)
    }

    print("Loading hero..")
    hero_img = 'assets/images/rpgsprites1/warrior_f.png'
    hero_animation = Animation(load_image(hero_img), 32, 36, hero_animations, random.randint(0, 1), 0.25)
    hero  = Hero(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2, surface, hero_animation)

    collidables = []
    # load entities from map

    # load tiles
    #  -base 
    # - ground
    # - hills ( this layer will have collision)
    # - PlayerData
    map_path = 'assets/tilesets/map-01.tmx'

    tiled_map = load_map(map_path)
    for layer in tiled_map.layers:

        print("Loading layer %s..." % layer.name) 

        if isinstance(layer,pytmx.TiledTileLayer):
            new_entities, new_collidables = load_tiles(layer)
            collidables += new_collidables
            entities += new_entities
        
        print("---")

    map_width = tiled_map.width * tiled_map.tilewidth
    map_height = tiled_map.height * tiled_map.tileheight
    camera = Camera(simple_camera, map_width, map_height)
    entities.append(hero)

    aiSystem = AiSystem([entity.controller for entity in entities if entity.controller])
    animationSystem = AnimationSystem([entity.renderer for entity in entities if entity.renderer])
    graphicsSystem = GraphicsSystem(surface, [entity.graphics for entity in entities if entity.graphics], camera)
    physicsSystem = PhysicsSystem([entity.physics for entity in entities if entity.physics], collidables)
    
    # tiles = [entity for entity in entities if entity != hero]
    # worldView = WorldView(hero, [0, 0], SCREEN_SIZE, tiles, 32)
    # hudView = HudView()

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

        camera.update(camera_target)
        
        for control_system in main_systems:
            control_system.update(delta_time)
       
        draw_debug(surface, font, hero)
        pygame.display.update()

        last_millis = FPS_CLOCK.tick(30)