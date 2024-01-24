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


class Bird(pygame.sprite.Sprite):
    image = load_image("bird_middle.png")
    image = pygame.transform.scale(image, (50, 50))

    def __init__(self, *group, up, coordx, coordy, v, fps):
        super().__init__(*group)

        self.image = Bird.image

        self.rect = self.image.get_rect()
        self.v = v
        self.fps = fps
        self.rect.x = coordx
        self.rect.y = coordy
        self.up = up
        self.isJump = False
        self.jumpCount = 10

    def update(self):

        if 550 >= self.rect.y >= 0:
            if self.isJump is True:

                if self.jumpCount >= 0:

                    if self.jumpCount < 0:

                        self.rect.y += self.v / self.fps

                    else:

                        self.rect.y -= self.v / self.fps

                    self.jumpCount -= 1

                else:

                    self.isJump = False
                    self.jumpCount = 10
            else:
                self.rect.y += self.v / self.fps
        else:

            sys.exit()
