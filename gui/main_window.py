from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QGridLayout,
    QMainWindow,
    QMenu,
    QMenuBar,
    QTabWidget,
    QWidget,
)

from gui.book_shelve import BookShelveShowWidget
from gui.information_widget import BookCatalogueInformationWidget
from gui.simple_search_widget import SimpleSearchWidget


class BookCatalogueMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Book Catalogue")
        self.setMinimumSize(480, 640)
        self.__init_main_menu()
        self.__init_main_widget()


    def __init_main_widget(self):
        self.__centralWidget = QWidget()
        self.setCentralWidget(self.__centralWidget)
        self.__centralWidget.setStyleSheet("background-color: #c6fad8;")
        self.__main_grid = QGridLayout(self.__centralWidget)
        self.__main_grid.setSpacing(2)

        self.__wd_search = SimpleSearchWidget()
        self.__main_grid.addWidget(self.__wd_search, 0, 0, 1, 10, Qt.AlignTop)

        self.__main_shelve_tab = QTabWidget()
        self.__main_grid.addWidget(self.__main_shelve_tab, 1, 0, 15, 10)

        self.__main_information_widget = BookCatalogueInformationWidget()
        self.__main_grid.addWidget(self.__main_information_widget, 16, 0, 1, 10, Qt.AlignBottom)
        self.setLayout(self.__main_grid)


    def __init_main_menu(self):
        menu_bar = QMenuBar(self)
        db_menu = QMenu("&DataBase", self)
        menu_bar.addMenu(db_menu)

        book_menu = db_menu.addMenu('Books')
        book_menu.addAction('New')
        book_menu.addAction('Search')

        author_menu = db_menu.addMenu('Authors')
        author_menu.addAction('New')
        author_menu.addAction('Search')

        import_menu = db_menu.addMenu('Imports')
        import_menu.addAction('JSON')
        import_menu.addAction('XML')
        import_menu.addAction('CSV')

        shelve_menu = QMenu("&BookShelve", self)
        menu_bar.addMenu(shelve_menu)
        shelve_menu.addAction('New')
        shelve_menu.addAction('Edit')
        shelve_menu.addAction('Delete')

        setting_menu = QMenu("&Setting", self)
        menu_bar.addMenu(setting_menu)

        help_menu = QMenu("&Help", self)
        menu_bar.addMenu(help_menu)

        self.setMenuBar(menu_bar)