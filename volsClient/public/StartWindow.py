# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from public import ManagerMainWindow, Login, GuestMainWindow


class StartWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, Main_window):
        Main_window.setObjectName("Main_window")
        Main_window.resize(300, 270)
        Main_window.setMinimumSize(QtCore.QSize(300, 270))
        Main_window.setMaximumSize(QtCore.QSize(300, 270))
        self.centralwidget = QtWidgets.QWidget(Main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 241, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.manager_enter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manager_enter.sizePolicy().hasHeightForWidth())
        self.manager_enter.setSizePolicy(sizePolicy)
        self.manager_enter.setObjectName("manager_enter")
        self.verticalLayout.addWidget(self.manager_enter)
        self.guest_enter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guest_enter.sizePolicy().hasHeightForWidth())
        self.guest_enter.setSizePolicy(sizePolicy)
        self.guest_enter.setObjectName("guest_enter")
        self.verticalLayout.addWidget(self.guest_enter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.btn_exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout.addWidget(self.btn_exit)
        Main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main_window)

        self.manager_enter.clicked.connect(self.manager_enter_click)
        self.guest_enter.clicked.connect(self.guest_enter_click)
        self.btn_exit.clicked.connect(self.btn_exit_click)
        QtCore.QMetaObject.connectSlotsByName(Main_window)

    def retranslateUi(self, Main_window):
        _translate = QtCore.QCoreApplication.translate
        Main_window.setWindowTitle(_translate("Main_window", "Вход"))
        self.manager_enter.setText(_translate("Main_window", "Управляющий"))
        self.guest_enter.setText(_translate("Main_window", "Гость"))
        self.btn_exit.setText(_translate("Main_window", "Выход"))

    #
    #   click events
    #
    def manager_enter_click(self):
        if Login.LoginWindow(self).exec_() == QtWidgets.QDialog().Accepted:
            self.window = ManagerMainWindow.ManagerMainWindow()
            self.window.show()
            self.close()

    def guest_enter_click(self):
        self.window = GuestMainWindow.GuestMainWindow()
        self.window.show()
        self.close()

    @staticmethod
    def btn_exit_click():
        sys.exit()
