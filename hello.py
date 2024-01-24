import sys
import sqlite3
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtWidgets import QInputDialog

complexity = "Базовый"


class Pages(QMainWindow):
    def __init__(self, strok):
        global complexity
        super().__init__()
        self.strok = strok
        self.setFixedSize(623, 700)
        uic.loadUi(self.strok, self)
        if self.strok == "hello_page.ui":
            self.page_id = 0
            self.pixmap = QPixmap('FL_bird.png')
            self.image = QLabel(self)
            self.image.move(0, 0)
            self.image.resize(623, 469)
            self.image.setPixmap(self.pixmap)
            self.show()
            self.complexity_Button.clicked.connect(self.run)
            self.startButton.setText(f"Начать игру\nУровень: {complexity}")

    def run(self):
        global complexity
        complexity, ok_pressed = QInputDialog.getItem(
            self, "Сложность", "Выберите уровень",
            ("Легкий", "Базовый", "Сложный"), 1, False)
        if ok_pressed:
            self.startButton.setText(f"Начать игру\nУровень: {complexity}")


app = QApplication(sys.argv)
hello_page = Pages("hello_page.ui")
sys.exit(app.exec_())
