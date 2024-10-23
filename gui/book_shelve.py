from PyQt5.QtWidgets import QGridLayout, QTableWidget, QWidget


class BookShelveShowWidget(QWidget):
    def __init__(self, name: str):
        super().__init__()
        self.__name_shelve = name
        self.setMinimumSize(480, 550)

        self.__main_grid = QGridLayout(self)

        self.__wd_statistics = QWidget()
        self.__wd_statistics.setMinimumWidth(100)
        self.__wd_statistics.setMinimumHeight(540)
        self.__main_grid.addWidget(self.__wd_statistics, 0, 0, 10, 1)

        self.__table_books = QTableWidget()
        self.__table_books.setMinimumWidth(270)
        self.__table_books.setMinimumHeight(540)
        self.__main_grid.addWidget(self.__table_books, 0, 1, 10, 3)

        self.__wd_book_info = QWidget()
        self.__wd_book_info.setMinimumSize(100, 540)
        self.__main_grid.addWidget(self.__wd_book_info, 0, 4, 10, 1)

        self.setLayout(self.__main_grid)


    @property
    def name(self) ->str:
        return self.__name_shelve
