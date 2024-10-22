from datetime import datetime

from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget
from PyQt5.QtCore import Qt


class BookCatalogueInformationWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(30)
        self.setMinimumWidth(470)

        self.__main_layout = QGridLayout(self)

        self.__lbl_count_book = QLabel()
        self.__lbl_count_book.setFixedHeight(25)
        self.__lbl_count_book.setMinimumWidth(150)
        self.__main_layout.addWidget(self.__lbl_count_book, 0, 0, 1, 1, alignment=Qt.AlignLeft)

        self.__lbl_size_book = QLabel()
        self.__lbl_size_book.setFixedHeight(25)
        self.__lbl_size_book.setMinimumWidth(150)
        self.__main_layout.addWidget(self.__lbl_size_book, 0, 1, 1, 1, alignment=Qt.AlignCenter)

        self.__lbl__datetime = QLabel()
        self.__lbl__datetime.setFixedHeight(25)
        self.__lbl__datetime.setMinimumWidth(140)
        self.__main_layout.addWidget(self.__lbl__datetime, 0, 2, 1, 1, alignment=Qt.AlignRight)

        self.set_count_book(0)
        self.set_size_book(0)
        self.set_datetime()

    def set_count_book(self, count: int):
        self.__lbl_count_book.setAlignment(Qt.AlignLeft)
        self.__lbl_count_book.setText(f'Количество книг: {count}.')

    def set_size_book(self, size: int):
        self.__lbl_size_book.setAlignment(Qt.AlignHCenter)
        self.__lbl_size_book.setText(f'Размер книг: {size}Б.')

    def set_datetime(self):
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
        self.__lbl__datetime.setAlignment(Qt.AlignRight)
        self.__lbl__datetime.setText(date_time)
