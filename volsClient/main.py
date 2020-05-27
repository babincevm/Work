# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from public import StartWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = StartWindow.StartWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
