import pygame
import os
import sys
import random


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

    def __init__(self, *group, up, coordx, coordy):
        super().__init__(*group)
        self.image = Tube.image
        self.rect = self.image.get_rect()
        self.rect.x = coordx
        self.rect.y = coordy
        self.up = up

    def update(self):
        if self.up:
            self.image = Tube.image2
        else:
            self.image = Tube.image

        if self.rect.x <= -100:
            self.rect.x = 1100
        else:
            self.rect.x -= v / fps


if __name__ == '__main__':
    tubes_sprites = pygame.sprite.Group()
    x_1 = 600
    for i in range(4):
        x_1 += 300
        y_1 = random.randrange(300, 500)
        Tube(tubes_sprites, up=False, coordx=x_1, coordy=y_1)
        Tube(tubes_sprites, up=True, coordx=x_1, coordy=y_1 - 700)

    fps = 60
    v = 400
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
        clock.tick(fps)
    pygame.quit()
