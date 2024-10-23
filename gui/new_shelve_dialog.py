from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QLabel, QLineEdit, QDialog, QDialogButtonBox, QGridLayout


class NewShelveWidget(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(QSize(300, 150))
        self.__name_book_shelve: str = ''
        self.setWindowTitle("New Book Shelve!")
        self.__main_grid = QGridLayout()
        self.__lbl_name = QLabel()
        self.__lbl_name.setFixedSize(QSize(140, 30))
        self.__lbl_name.setText('Имя книжной полки:')
        self.__lbl_name.setAlignment(Qt.AlignRight)
        self.__main_grid.addWidget(self.__lbl_name, 0, 0, 1, 1)

        self.__led_name = QLineEdit()
        self.__led_name.setFixedSize(140, 30)
        self.__main_grid.addWidget(self.__led_name, 0, 1, 1, 1)

        self.__button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.__main_grid.addWidget(self.__button_box, 1, 0, 1, 2)
        self.__button_box.accepted.connect(self.accept)
        self.__button_box.rejected.connect(self.reject)

        self.setLayout(self.__main_grid)

    def show(self):
        self.__led_name.clear()
        super().show()

    @property
    def name(self) ->str:
        return self.__name_book_shelve

    def accept(self):
        self.__name_book_shelve = self.__led_name.text()
        if self.__name_book_shelve:
            self.done(1)
        else:
            self.done(0)
