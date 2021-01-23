from lib.navigation import NORTH, SOUTH, EAST, WEST
import pygame as pg
import math
"""
Sprite loading tools

sprite map example
-----------------

each sprite has a two frame animation

5 x 5 sprite map
32 x 32 sprites

i i u u d
d l l r r
1 1 2 2 3
3 4 4 

i - idle

u - walk up
d - walk down
l - walk left
r - walk right

1 - attack up
2 - attack down
3 - attack left
4 - attack right

"""

N_ANIM = 'n'
S_ANIM = 's'
E_ANIM = 'e'
W_ANIM = 'w'

class Animation:
    def __init__(self, img, width, height, animations=None, frame=0, speed=0.125, start_animation=E_ANIM):
        """
        This class must have a sprite sheet with at least one animation
        Args:
            img: pygame.image of the sprite sheet
            animations: dict of animation tuples containing an offset and length, using animation names as the keys
            frame: current frame of animation to be on
            clip_lenght: the lenght of the animation
            speed: the speed at which the animation should run.
        """
        self.img = img
        # self.img.set_colorkey((236, 236, 236))

        self.current_animation = start_animation
        self.width = width
        self.height = height
        self.frame = frame
        self.speed = speed
        self.timer = 0
        self.direction = (0,1)

        if animations:
            self.anims = animations
        else:
            self.anims = { E_ANIM: (0,1) }

    def get_frame(self):
        return self.get_offset() + self.frame

    def get_offset(self):
        return self.anims[self.current_animation][0]

    def get_animation_length(self):
        return self.anims[self.current_animation][1]

    def next_frame(self):
        self.timer = 0 
        self.frame += 1
        self.frame %= self.get_animation_length()

    def get_timer(self):
        return self.timer

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed
    
    def get_rect(self):
        return pg.Rect(self.get_x(), self.get_y(), self.width, self.height)

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def get_x(self):
        return self.get_frame() % (self.img.get_width()/self.width) * self.width

    def get_y(self):
        return math.floor(self.get_frame() / (self.img.get_width() / self.width)) * self.height

    def update(self, delta_time):
        self.timer += delta_time
        self.update_direction()
        # update animation
        if self.timer >= self.speed:
            self.next_frame()


    def update_direction(self):
        """
        based upon the direction of the entity pull the right frame offset
        """
        direction = self.get_direction()

        if direction[1] == NORTH[1]:
            self.current_animation = N_ANIM 
        elif direction[1] == SOUTH[1]:
            self.current_animation = S_ANIM 
        elif direction[0] == EAST[0]:
            self.current_animation = E_ANIM 
        else:
            self.current_animation = W_ANIM 

