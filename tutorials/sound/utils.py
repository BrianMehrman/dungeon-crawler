import pygame, os

local_dir = os.path.dirname(__file__)

def local_file(path):
    return os.path.join(local_dir, path)

def load_image(file_name):
    lfile = local_file(file_name)
    print(lfile)
    return pygame.image.load(lfile)