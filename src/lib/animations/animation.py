
"""
Sprite loading tools
"""

class animation:
    def __init__(self, img, frame, clip_length, speed=0.125):
        self.frame = frame
        self.speed = speed
        self.clip_length = clip_length
        self.timer = 0

    def get_frame(self):
        return self.frame

    def next_frame(self):
        self.timer = 0 
        self.frame += 1
        self.frame %= clip_length

    def get_timer(self):
        return self.timer

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed
    