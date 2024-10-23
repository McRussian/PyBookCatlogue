from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QGridLayout,
    QLabel,
    QLineEdit,
)

from models.author import Author


class AuthorShowDialog(QDialog):
    def __init__(self, author: Author=Author(), parent=None):
        super().__init__(parent)
        self.__author = author
        self.setFixedSize(QSize(400, 350))

        self.setWindowTitle('Author')
        self.__main_grid = QGridLayout()

        self.__lbl_first_name = QLabel()
        self.__lbl_first_name.setFixedSize(QSize(140, 30))
        self.__lbl_first_name.setAlignment(Qt.AlignRight)
        self.__lbl_first_name.setText('First Name:')
        self.__main_grid.addWidget(self.__lbl_first_name, 0, 0, 1, 1)
        self.__led_first_name = QLineEdit()
        self.__led_first_name.setFixedSize(200, 30)
        self.__main_grid.addWidget(self.__led_first_name, 0, 1, 1, 1)

        self.__lbl_last_name = QLabel()
        self.__lbl_last_name.setFixedSize(QSize(140, 30))
        self.__lbl_last_name.setAlignment(Qt.AlignRight)
        self.__lbl_last_name.setText('Last Name:')
        self.__main_grid.addWidget(self.__lbl_last_name, 1, 0, 1, 1)
        self.__led_last_name = QLineEdit()
        self.__led_last_name.setFixedSize(200, 30)
        self.__main_grid.addWidget(self.__led_last_name, 1, 1, 1, 1)

        self.__lbl_middle_name = QLabel()
        self.__lbl_middle_name.setFixedSize(QSize(140, 30))
        self.__lbl_middle_name.setAlignment(Qt.AlignRight)
        self.__lbl_middle_name.setText('Last Name:')
        self.__main_grid.addWidget(self.__lbl_middle_name, 2, 0, 1, 1)
        self.__led_middle_name = QLineEdit()
        self.__led_middle_name.setFixedSize(200, 30)
        self.__main_grid.addWidget(self.__led_middle_name, 2, 1, 1, 1)

        self.__lbl_alias = QLabel()
        self.__lbl_alias.setFixedSize(QSize(140, 30))
        self.__lbl_alias.setAlignment(Qt.AlignRight)
        self.__lbl_alias.setText('Alias:')
        self.__main_grid.addWidget(self.__lbl_alias, 3, 0, 1, 1)
        self.__led_alias = QLineEdit()
        self.__led_alias.setFixedSize(200, 30)
        self.__main_grid.addWidget(self.__led_alias, 3, 1, 1, 1)

        self.__button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.__main_grid.addWidget(self.__button_box, 5, 0, 1, 2)
        self.__button_box.accepted.connect(self.accept)
        self.__button_box.rejected.connect(self.reject)

        self.setLayout(self.__main_grid)

        self.init_author_data(self.__author)

    def init_author_data(self, author: Author):
        self.__led_first_name.setText(author.first_name)
        self.__led_last_name.setText(author.last_name)
        self.__led_middle_name.setText(author.middle_name)
        self.__led_alias.setText(author.alias)

    @property
    def author(self) ->Author:
        return self.__author

    def accept(self):
        self.__author.set_first_name(self.__led_first_name.text())
        self.__author.set_last_name(self.__led_last_name.text())
        self.__author.set_middle_name(self.__lbl_middle_name.text())
        self.__author.set_alias(self.__led_alias.text())

        self.done(1)
