"""
Файл для повторения темы генерации сигналов и передачи данных из одного виджета в другой

Напомнить про работу с пользовательскими сигналами.

Предлагается создать 2 формы:
* На первый форме label с надписью "Пройдите регистрацию" и pushButton с текстом "Зарегистрироваться"
* На второй (QDialog) форме:
  * lineEdit с placeholder'ом "Введите логин"
  * lineEdit с placeholder'ом "Введите пароль"
  * pushButton "Зарегистрироваться"

  при нажатии на кнопку, данные из lineEdit'ов передаются в главное окно, в
  котором надпись "Пройдите регистрацию", меняется на "Добро пожаловать {данные из lineEdit с логином}"
  (пароль можно показать в терминале в захешированном виде)
"""

from PySide6 import QtWidgets, QtCore
from dialog import Ui_Dialog


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUi()
        self.__initSignals()

    def __initUi(self):
        self.setFixedSize(300, 100)
        self.setWindowTitle("Окно 1")
        label = QtWidgets.QLabel(self)
        label.setText("<h1>Пройдите регистрацию</h1>")

        self.__pushButton = QtWidgets.QPushButton(self)
        self.__pushButton.setText("Зарегистрироваться")
        self.__pushButton.move(100, 50)

    def __initSignals(self):
        self.__pushButton.clicked.connect(self.open_child_window)
        self.child_window.custom_signal.connect(self.textSignal)


    def open_child_window(self):
        self.child_window = OtherWindow()
        self.child_window.show()


    def textSignal(self, text):
        self.label.setText(text)



class OtherWindow(QtWidgets.QWidget):
    custom_signal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def initSignalsOther(self):
        self.ui.pushButton.clicked.connect(self.changedLineEditText)

    def changedLineEditText(self):
        self.custom_signal.emit(self.lineEdit.text())




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
