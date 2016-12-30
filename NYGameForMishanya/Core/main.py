import random
import pygame
import blocks_fabric
import character
from blocks import *

WIN_WIDTH = 1000
WIN_HEIGHT = 650
WINDOW = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW)
    pygame.display.set_caption("Happy New Year 2017!")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))
    bg = image.load("../Sources/bg_books.jpg")

    pic = pygame.image.load("../Sources/bg_books.jpg")
    screen.blit(pygame.transform.scale(pic, (500, 500)), (0, 0))

    hero = character.Character()
    left = right = up = down = False
    block_counter = 0
    timer = pygame.time.Clock()
    objects = pygame.sprite.Group()
    platforms = []
    borders = []
    objects.add(hero)

    y = x = 0
    for i in range(int(WIN_HEIGHT / BLOCK_HEIGHT)+1):
        left_border = Platform(-BLOCK_WIDTH, y)
        right_border = Platform(WIN_WIDTH, y)
        objects.add(left_border, right_border)
        borders.append(left_border)
        borders.append(right_border)
        y += BLOCK_HEIGHT
    for i in range(int(WIN_WIDTH / BLOCK_WIDTH)+1):
        top_border = Platform(x, -BLOCK_HEIGHT)
        bottom_border = Platform(x, WIN_HEIGHT)
        objects.add(top_border, bottom_border)
        borders.append(top_border)
        borders.append(bottom_border)
        x += BLOCK_WIDTH

    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit, "QUIT"

            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_UP:
                up = True

            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_UP:
                up = False

        screen.blit(bg, (0, 0))
        collision_fact = hero.update(left, right, up, down, WIN_WIDTH, WIN_HEIGHT, platforms)
        if collision_fact:
            hero.rect.x = hero.startX
            hero.rect.y = hero.startY
            hero.score -= 50
            hero.hp -= 250
        objects.draw(screen)
        pygame.display.update()
        if block_counter % 15 == 0:
            block = blocks_fabric.block_generate()
            objects.add(block)
            platforms.append(block)
            block_counter = 0
        for platform in platforms:
            platform.rect.y += 5
        block_counter += 1
        timer.tick(60)


if __name__ == "__main__":
    main()
