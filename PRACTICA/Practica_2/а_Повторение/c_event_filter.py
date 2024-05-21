"""
Файл для повторения темы фильтр событий

Напомнить про работу с фильтром событий.

Предлагается создать кликабельный QLabel с текстом "Красивая кнопка",
используя html - теги, покрасить разные части текста на нём в разные цвета
(красивая - красным, кнопка - синим)
"""
import sys

from PySide6 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUi()

    def __initUi(self):
        self.setFixedSize(300, 300)
        self.setMouseTracking(True)

        self.label = QtWidgets.QLabel('<h1>Красивая кнопка</h>')
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        laout = QtWidgets.QVBoxLayout()
        laout.addWidget(self.label)

        self.setLayout(laout)



        # self.label = QtWidgets.QLabel(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
