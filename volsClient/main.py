# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from public import StartWindow
import traceback


def main():
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = StartWindow.StartWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception:
        print(traceback.format_exc())


if __name__ == '__main__':
    main()
