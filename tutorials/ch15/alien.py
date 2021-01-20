
class Alien():
    def __init__(self, x, y, width=24, height=24):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

    def draw(self):
        return "o"

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width