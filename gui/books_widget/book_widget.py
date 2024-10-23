from PyQt5.QtWidgets import QLabel, QTextBrowser, QWidget
from PyQt5.QtCore import QSize


class BookShowWidget(QWidget):
    def __init__(self, width: int = 60, height: int = 100):
        super().__init__()
        self.__width = width
        self.__height = height
        self.setFixedSize(QSize(self.__width, self.__height))

        self.__lbl_title = QLabel(self)
        self.__lbl_title.setGeometry(5, 5, self.__width - 10, 20)

        self.__lbl_author = QLabel(self)
        self.__lbl_author.setGeometry(5, 30, self.__width - 10, 20)

        self.__txt_description = QTextBrowser(self)
        self.__txt_description.setGeometry(5, 55, self.__width - 10, self.__height - 60)

    def set_author(self, names: list[str]):
        self.__lbl_author.setText('; '.join(names))

    def set_title(self, title: str):
        self.__lbl_title.setText(title)

    def set_description(self, description: list[str]):
        self.__txt_description.setText('/n'.join(description))