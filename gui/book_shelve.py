from PyQt5.QtWidgets import QHBoxLayout, QTableWidget, QWidget
from PyQt5.QtCore import Qt

from gui.book_widget import BookShowWidget


class BookShelveShowWidget(QWidget):
    def __init__(self, name: str):
        super().__init__()
        self.__name_shelve = name
        self.setMinimumSize(480, 600)

        self.__main_layout = QHBoxLayout(self)

        self.__wd_statistics = QWidget()
        self.__wd_statistics.setMinimumWidth(100)
        self.__wd_statistics.setMinimumHeight(590)
        self.__main_layout.addWidget(self.__wd_statistics, stretch=5, alignment=Qt.AlignLeft)

        self.__table_books = QTableWidget()
        self.__table_books.setMinimumSize(270, 590)
        self.__main_layout.addWidget(self.__table_books, stretch=5, alignment=Qt.AlignCenter)

        self.__wd_book_info = QWidget()
        self.__wd_book_info.setMinimumSize(100, 590)
        self.__main_layout.addWidget(self.__wd_book_info, stretch=5, alignment=Qt.AlignRight)


    @property
    def name(self) ->str:
        return self.__name_shelve
