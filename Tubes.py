import os
import sys

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    # если файл не существует, то выходим

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)
    return image


class Tube(pygame.sprite.Sprite):
    image = load_image("tube3.png")
    image = pygame.transform.scale(image, (100, 500))
    image2 = pygame.transform.flip(image, 0, 1)

    def __init__(self, *group, up, coordx, coordy, v, fps):
        super().__init__(*group)
        self.image = Tube.image
        self.rect = self.image.get_rect()
        self.v = v
        self.fps = fps
        self.rect.x = coordx
        self.rect.y = coordy
        self.up = up
        self.counter = 0

    def update(self):
        if self.up:

            self.image = Tube.image2

        else:

            self.image = Tube.image

        if self.rect.x <= -100:

            self.rect.x = 1100
        else:
            if self.v != 0:
                self.rect.x -= 4
