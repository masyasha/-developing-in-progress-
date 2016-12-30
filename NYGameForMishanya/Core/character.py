from pygame import *
import main

WIN_WIDTH = 1000
WIN_HEIGHT = 650

MOVE_SPEED = 5
CHARACTER_WIDTH = 22
CHARACTER_HEIGHT = 32
CHARACTER_COLOR = "#888888"
START_X = (WIN_WIDTH / 2) - (CHARACTER_WIDTH / 2)
START_Y = WIN_HEIGHT - CHARACTER_HEIGHT - 20


class Character(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.x_velocity = 0
        self.y_velocity = 0
        self.startX = START_X
        self.startY = START_Y
        self.image = Surface((CHARACTER_WIDTH, CHARACTER_HEIGHT))
        self.image.fill(Color(CHARACTER_COLOR))
        self.image = image.load("../Sources/plane.png")
        self.rect = Rect(self.startX, self.startY, CHARACTER_WIDTH, CHARACTER_HEIGHT)
        self.hp = 1000
        self.score = 0

    def update(self, left, right, up, down, win_width, win_height, platforms):
        if left:
            self.x_velocity = -MOVE_SPEED

        if right:
            self.x_velocity = MOVE_SPEED

        if not (left or right):
            self.x_velocity = 0

        if up:
            self.y_velocity = -MOVE_SPEED

        if down:
            self.y_velocity = MOVE_SPEED

        if not (up or down):
            self.y_velocity = 0

        self.rect.y += self.y_velocity
        collision_fact_y = self.collide(0, self.y_velocity, platforms)

        self.rect.x += self.x_velocity
        collision_fact_x = self.collide(self.x_velocity, 0, platforms)

        if collision_fact_x or collision_fact_y:
            return True

    def collide(self, x_velocity, y_velocity, platforms):
        for block in platforms:
            if sprite.collide_rect(self, block):

                if x_velocity > 0:
                    self.rect.right = block.rect.left

                if x_velocity < 0:
                    self.rect.left = block.rect.right

                if y_velocity > 0:
                    self.rect.bottom = block.rect.top

                if y_velocity < 0:
                    self.rect.top = block.rect.bottom

                return True

