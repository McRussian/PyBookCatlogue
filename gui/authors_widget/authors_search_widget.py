from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QCheckBox,
    QWidget,
    QPushButton,
    QGridLayout,
    QLabel,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
)

from gui.authors_widget.authors_filter_widget import AuthorFilterWidget
from models.author import Author


class AuthorSearchWidget(QWidget):
    def __init__(self, authors: list[Author]=[]):
        super().__init__()
        self.__authors = authors
        self.setMinimumSize(QSize(440, 350))
        self.setStyleSheet("background-color: #b4ffc0;")
        self.setWindowTitle('Author Search')
        self.__init_widget()

    def __init_widget(self):
        self.__main_grid = QGridLayout(self)
        self.__table_authors = QTableWidget()
        self.__table_authors.setMinimumWidth(300)
        self.__table_authors.setMinimumHeight(300)
        self.__main_grid.addWidget(self.__table_authors, 0, 0, 8, 3)

        self.__filter_widget = AuthorFilterWidget()
        self.__main_grid.addWidget(self.__filter_widget, 0, 4, 4, 1)

        self.__btn_add = QPushButton()
        self.__btn_add.setMinimumSize(QSize(80, 40))
        self.__btn_add.setText("Add")
        self.__main_grid.addWidget(self.__btn_add, 4, 4, 1, 1)

        self.__btn_edit = QPushButton()
        self.__btn_edit.setMinimumSize(QSize(80, 40))
        self.__btn_edit.setText("Edit")
        self.__main_grid.addWidget(self.__btn_edit, 5, 4, 1, 1)

        self.__btn_delete = QPushButton()
        self.__btn_delete.setMinimumSize(QSize(80, 40))
        self.__btn_delete.setText("Delete")
        self.__main_grid.addWidget(self.__btn_delete, 6, 4, 1, 1)

        self.__btn_select = QPushButton()
        self.__btn_select.setMinimumSize(QSize(80, 40))
        self.__btn_select.setText("Select")
        self.__main_grid.addWidget(self.__btn_select, 7, 4, 1, 1)

        self.setLayout(self.__main_grid)


    def set_authors(self, authors: list[Author]):
        self.__authors = authors

    def __fill_table_author(self):
        pass

    def __clear_table_authors(self):
        pass
