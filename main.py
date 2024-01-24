import pygame
import os
import sys
import random
from Tubes import Tube
import sys
from PyQt5.QtWidgets import QApplication
from hello import Pages


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    tubes_sprites = pygame.sprite.Group()
    x_1 = 600
    for i in range(4):
        x_1 += 300
        y_1 = random.randrange(300, 500)
        Tube(tubes_sprites, up=False, coordx=x_1, coordy=y_1, v=400, fps=60)
        Tube(tubes_sprites, up=True, coordx=x_1, coordy=y_1 - 700, v=400, fps=60)

    pygame.init()
    size = width, height = 1100, 600
    gol_color = [150, 200, 250]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(gol_color)
        tubes_sprites.update()
        tubes_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
