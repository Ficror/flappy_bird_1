import pygame
import os
import sys
import random

from Bird import Bird
from Tubes import Tube
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def draw(screen):
    font = pygame.font.Font(None, 80)
    text = font.render(f'Результат: {str(counter)}', True, (0, 0, 0))
    text_x = 400
    text_y = 50
    screen.blit(text, (text_x, text_y))


if __name__ == '__main__':
    v_0 = 0
    #ЭТО НАЧАЛЬНАЯ СКОРОСТЬ. ПОКА ВЫПОЛНЯЕТСЯ ПРОГРАММА В QT ЭТОТ ПАРАМЕТР РАВЕН 0, А КОГДА ОКНО QT СВОРАЧИВАЕТСЯ ПРИДАЕМ ЗНАЧЕНИЕ СКОРОСТИ 350
    #
    #
    #
    v_0 = 350
    x_1 = 600
    y_1 = 200
    size = width, height = 1100, 600
    gol_color = [150, 200, 250]
    counter = 0
    coords_of_bird = 600

    tubes_sprites = pygame.sprite.Group()
    bird_sprite = pygame.sprite.Group()
    bird = Bird(bird_sprite, up=True, coordx=x_1, coordy=y_1, v=v_0, fps=60)

    for i in range(4):
        x_1 += 300
        y_1 = random.randrange(300, 500)
        Tube(tubes_sprites, up=False, coordx=x_1, coordy=y_1, v=v_0, fps=100)
        Tube(tubes_sprites, up=True, coordx=x_1, coordy=y_1 - 680, v=v_0, fps=100)

    pygame.init()
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                bird.isJump = True
        if pygame.sprite.spritecollideany(bird, tubes_sprites) is not None:
            sys.exit()
        for i in tubes_sprites.sprites():
            if i.rect.x == bird.rect.x:
                counter += 1
                if counter % 4 == 0:
                    coords_of_bird += 50
                break

        screen.fill(gol_color)
        tubes_sprites.update()
        tubes_sprites.draw(screen)
        bird_sprite.update()
        bird_sprite.draw(screen)
        draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
