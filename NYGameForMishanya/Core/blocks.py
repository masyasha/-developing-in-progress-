from pygame import *

BLOCK_WIDTH = 20
BLOCK_HEIGHT = 20
BLOCK_COLOR = "#FF6262"


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((BLOCK_WIDTH, BLOCK_HEIGHT))
        self.image.fill(Color(BLOCK_COLOR))
        self.rect = Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)




