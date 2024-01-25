import sys
import sqlite3
import os
import sys
from Bird import Bird
from Tubes import Tube
import pygame
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QTimer
import random
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtWidgets import QInputDialog

complexity = "Базовый"

con = sqlite3.connect("record.db")

cur = con.cursor()


class Game():
    def __init__(self):
        pygame.init()
        self.game_init()

    def game_init(self):
        self.x_1 = 600
        self.y_1 = 100
        self.size = self.width, self.height = 1100, 600
        self.gol_color = [150, 200, 250]
        self.counter = 0
        self.coords_of_bird = 600

        self.tubes_sprites = pygame.sprite.Group()
        self.bird_sprite = pygame.sprite.Group()
        self.bird = Bird(self.bird_sprite, up=True, coordx=self.x_1, coordy=self.y_1, v=350, fps=60)

        for i in range(4):
            self.x_1 += 300
            self.y_1 = random.randrange(300, 500)
            Tube(self.tubes_sprites, up=False, coordx=self.x_1, coordy=self.y_1, v=200, fps=100)
            Tube(self.tubes_sprites, up=True, coordx=self.x_1, coordy=self.y_1 - 700, v=200, fps=100)

        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

    def loop(self, window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.bird.isJump = True
        self.screen.fill([0, 0, 255])
        if pygame.sprite.spritecollideany(self.bird, self.tubes_sprites) is not None:
            '''again_page.score.setText(f"Score: {self.counter}")
            if self.counter > again_page.r:
                again_page.record.setText(f"Score: {self.counter}")
                inf = """INSERT INTO record (point) 
                                        VALUES (?);"""

                cur.execute(inf, self.counter)
                con.commit()'''
            again_page.setVisible(True)
            return True
        for i in self.tubes_sprites.sprites():
            if i.rect.x == self.bird.rect.x:
                self.counter += 1
                if self.counter % 4 == 0:
                    self.coords_of_bird += 50
                break

        self.screen.fill(self.gol_color)
        self.tubes_sprites.update()
        self.tubes_sprites.draw(self.screen)
        self.bird_sprite.update()
        self.bird_sprite.draw(self.screen)
        self.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)
        pygame.display.update()
        return False

    def draw(self, screen):
        font = pygame.font.Font(None, 80)
        text = font.render(f'Результат: {str(self.counter)}', True, (0, 0, 0))
        text_x = 400
        text_y = 50
        screen.blit(text, (text_x, text_y))


class HelloPage(QMainWindow):
    def __init__(self):
        super().__init__()
        global complexity
        super().__init__()
        self.setFixedSize(623, 700)
        uic.loadUi('hello_page.ui', self)
        self.page_id = 0
        self.pixmap = QPixmap('FL_bird.png')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(623, 469)
        self.image.setPixmap(self.pixmap)
        self.show()
        self.complexity_Button.clicked.connect(self.run)
        self.startButton.setText(f"Начать игру\nУровень: {complexity}")
        self.init_ui()

    def run(self):
        global complexity
        complexity, ok_pressed = QInputDialog.getItem(
            self, "Сложность", "Выберите уровень",
            ("Легкий", "Базовый", "Сложный"), 1, False)
        if ok_pressed:
            self.startButton.setText(f"Начать игру\nУровень: {complexity}")

    def init_ui(self):
        self.startButton.clicked.connect(self.openGame)
        self.show()

    def init_pygame(self):
        self.game = Game()
        self.timer = QTimer()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(10)

    def pygame_loop(self):
        if self.game.loop(self):
            self.timer.stop()
            self.timer.disconnect()
            pygame.quit()

    def openGame(self):
        self.setVisible(False)
        self.init_pygame()


class GameOverPage(QMainWindow):
    def __init__(self):
        super().__init__()
        global complexity
        super().__init__()
        self.setFixedSize(623, 700)
        uic.loadUi('game_over_page.ui', self)
        self.home_Button.clicked.connect(self.run)
        '''self.r = sum(list(cur.execute("""select point from record
                    """).fetchall()))
        self.record.setText(f"Record: {self.r}")'''
        self.init_ui()
        self.setVisible(False)

    def run(self):
        self.setVisible(False)
        ex.setVisible(True)

    def init_ui(self):
        self.start_againButton.clicked.connect(self.openGame)
        self.show()

    def init_pygame(self):
        self.game = Game()
        self.timer = QTimer()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(10)

    def pygame_loop(self):
        if self.game.loop(self):
            self.timer.stop()
            self.timer.disconnect()
            pygame.quit()

    def openGame(self):
        self.setVisible(False)
        self.init_pygame()


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = HelloPage()
    again_page = GameOverPage()
    result = app.exec_()
    sys.exit(result)
