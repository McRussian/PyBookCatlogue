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


class AuthorFilterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(QSize(80, 120))
        self.__main_grid = QGridLayout(self)

        self.__btn_filter = QPushButton()
        self.__btn_filter.setMinimumSize(QSize(80, 40))
        self.__btn_filter.setText("Filter")
        self.__main_grid.addWidget(self.__btn_filter, 4, 0, 1, 1)

        self.setLayout(self.__main_grid)