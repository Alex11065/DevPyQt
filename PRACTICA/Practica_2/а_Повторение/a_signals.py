"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets, QtGui
from PRACTICA.Practica_2.а_Повторение.ui.test import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.setText("Delete")
        self.ui.pushButton.clicked.connect(self.clear_button)
        self.ui.lineEdit.textEdited.connect(self.mirror)
        self.ui.lineEdit_2.textEdited.connect(self.ui.lineEdit.setText)

    def mirror(self):
        input_text = self.ui.lineEdit.text()[::-1]
        print(input_text)
        self.ui.lineEdit_2.setText(input_text)

    def clear_button(self):  # эксперимент
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        print("Данные удалены успешно!!!")

    def closeEvent(self, event: QtGui.QCloseEvent):
        print("Окно закрыто")




    #
    #     self.__initUi()
    #     self.__initSignals()
    #
    # def __initUi(self):
    #     self.lineEditInput = QtWidgets.QLineEdit()
    #     self.lineEditMirror = QtWidgets.QLineEdit()
    #
    #     self.pushButtonMirror = QtWidgets.QPushButton('Mirror')
    #     self.pushButtonClear = QtWidgets.QPushButton('Clear')
    #
    # def __initSignals(self):
    #     pass
    #
    # def __onPushButtonMirrorClicked(self):
    #     pass
    #
    # def __onPushButtonClearClicked(self):
    #     pass
    #
    # def __onLineEditMirrorTextChanged(self, text):
    #     print(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
