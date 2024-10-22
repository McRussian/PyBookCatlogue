from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QWidget, QPushButton



class SimpleSearchWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(30)
        self.setMinimumWidth(470)

        self.__main_layout = QHBoxLayout(self)

        self.__btn_full_search = QPushButton()
        self.__btn_full_search.setFixedSize(QSize(20, 20))
        self.__main_layout.addWidget(self.__btn_full_search, stretch=5, alignment=Qt.AlignLeft)

        self.__led_search = QLineEdit()
        self.__led_search.setFixedHeight(20)
        self.__led_search.setMinimumWidth(360)
        self.__main_layout.addWidget(self.__led_search, stretch=5)

        self.__btn_simple_search = QPushButton()
        self.__btn_simple_search.setFixedSize(QSize(70, 20))
        self.__btn_simple_search.setText('search')
        self.__main_layout.addWidget(self.__btn_simple_search, stretch=5, alignment=Qt.AlignRight)

