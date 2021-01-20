import pygame, sys

from views.robot_view import RobotView
from views.radar_view import RadarView
from controllers.robots_controller import RobotController
from robot_generator import RobotGenerator

pygame.init()

screen_size = (640, 480)
fps_clock = pygame.time.Clock()
surface = pygame.display.set_mode(screen_size)

last_millis = 0

generator = RobotGenerator()
view = RobotView('robotframes.png')
radar = RadarView('blip.png', 'radar.png')
controller = RobotController(generator.get_robots())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    delta_time = last_millis / 1000

    generator.update(delta_time)
    controller.update(delta_time)

    surface.fill((0, 0, 0))

    view.draw(surface, generator.get_robots())
    radar.draw(surface, generator.get_robots())

    pygame.display.update()

    last_millis = fps_clock.tick(30)