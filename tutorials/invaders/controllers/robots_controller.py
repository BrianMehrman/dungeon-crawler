from models.robot import Robot

class RobotController(object):
    
    def __init__(self, robots):
        self.robots = robots

    def update(self, delta_time):
        for robot in self.robots:
            robot.timer += delta_time
            if robot.get_timer() >= 0.125:
                robot.next_frame()

            pos = robot.get_position()

            speed = self.multiply(robot.get_speed(), delta_time) 
            x, y = self.add(pos, speed)

            sx, sy = robot.get_speed()

            if x < 0:
                x = 0
                sx *= -1
            elif x > 607:
                x = 607
                sx *= -1
            if y < 0:
                y = 0
                sy *= -1
            elif y > 447:
                y = 447
                sy *= -1

            robot.set_position((x, y))
            robot.set_speed((sx, sy))


    def multiply(self, speed, delta_time):
        x = speed[0] * delta_time
        y = speed[1] * delta_time

        return (x, y)

    def add(self, position, speed):
        x = position[0] + speed[0]
        y = position[1] + speed[1]

        return (x, y)

    