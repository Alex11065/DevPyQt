"""
Файл для повторения темы событий

Напомнить про работу с событиями.

Предлагается создать приложение, которое будет показывать все события происходящие в приложении,
(переопределить метод event), вывод событий производить в консоль.
При выводе события указывать время, когда произошло событие.
"""

from PySide6 import QtWidgets, QtCore, QtGui
import time


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

    #     self.initUi()
    #
    # def initUi(self) -> None:
    #     self.setFixedSize(300, 100)
    #     layout = QtWidgets.QVBoxLayout()
    #     self.pushButton = QtWidgets.QPushButton("Жмякни")
    #
    #     layout.addWidget(self.pushButton)
    #     self.setLayout(layout)
    #
    #     self.pushButton.clicked.connect(self.mousClick)
    # def mousClick(self):
    #     print(time.ctime(), 'mousClick', sep='-'*6)

    def event(self, event: QtCore.QEvent):
        print(time.ctime(), event)
        return super().event(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
