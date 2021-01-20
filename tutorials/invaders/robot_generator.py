import random
from  models.robot import Robot

class RobotGenerator(object):

    def __init__(self, generation_time = 1, max_robots = 10):
        self.robots = []
        self.generation_time = generation_time
        self.max_robots = max_robots
        self.counter = 0

    def get_robots(self):
        return self.robots

    def update(self, delta_time):
        self.counter += delta_time

        if self.counter >= self.generation_time and len(self.robots) < self.max_robots:
            self.counter = 0
            x = random.randint(36, 600)
            y = random.randint(36, 440)

            frame = random.randint(0, 1)

            sx = -50 + random.random() * 100
            sy = -50 + random.random() * 100

            new_robot = Robot(x, y, frame, (sx, sy))

            self.robots.append(new_robot)