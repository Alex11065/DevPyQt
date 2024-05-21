"""
Файл для повторения темы QSettings

Напомнить про работу с QSettings.

Предлагается создать виджет с plainTextEdit на нём, при закрытии приложения,
сохранять введённый в нём текст с помощью QSettings, а при открытии устанавливать
в него сохранённый текст
"""

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QSettings


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()
        self.ip_list_settings = QSettings("MyCompany", "MyApp")


    def __initUi(self):
        self.setFixedSize(300, 300)
        self.setWindowTitle('Окно')
        self.ip_list = self.ip_list_settings.value("ip_list", [])
        layout = QtWidgets.QVBoxLayout()
        self.lineEdit = QtWidgets.QLineEdit()
        if self.ip_list:
            self.lineEdit.setText(self.ip_list[0])
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)





    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        pass


    # def __loadSettings(self):
    #  pass


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

