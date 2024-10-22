import sys
from PyQt5.QtWidgets import QApplication

from gui.main_window import BookCatalogueMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = BookCatalogueMainWindow()
    w.show()

    sys.exit(app.exec_())
