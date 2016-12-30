import random
import pygame
from pygame import *
from main import *

BLOCK_COLOR = "#FFFFFF"
CUBE_MIN_SIDE = 5
CUBE_MAX_SIDE = 30
RECT_MAX_WIDTH = 500
RECT_MAX_HEIGHT = 50


class Cube(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.width = self.height = random.randint(CUBE_MIN_SIDE, CUBE_MAX_SIDE)
        self.x = random.randint(0, (WIN_WIDTH - self.width))
        self.y = -self.height
        self.image = Surface((self.width, self.height))
        self.image.fill(Color(BLOCK_COLOR))
        self.rect = Rect(self.x, self.y, self.width, self.height)


class Rectangle(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.width = random.randint(2, RECT_MAX_WIDTH)
        self.height = random.randint(2, RECT_MAX_HEIGHT)
        self.x = random.randint(0, (WIN_WIDTH - self.width))
        self.y = -self.height
        self.image = Surface((self.width, self.height))
        self.image.fill(Color(BLOCK_COLOR))
        self.rect = Rect(self.x, self.y, self.width, self.height)


def block_generate():
    objects = { 1: Cube,
                2: Rectangle }
    platform = objects[random.randint(1, 2)]()
    return platform













