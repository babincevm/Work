# -*- coding: utf-8 -*-
from views import add_window
from PyQt5 import QtCore, QtWidgets


class AddLevelWindow(QtWidgets.QDialog):
    def __init__(self, parent):
        super(AddLevelWindow, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, AddLevelWindow):
        AddLevelWindow.setObjectName("AddLevelWindow")
        AddLevelWindow.resize(360, 170)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddLevelWindow.sizePolicy().hasHeightForWidth())
        AddLevelWindow.setSizePolicy(sizePolicy)
        AddLevelWindow.setMinimumSize(QtCore.QSize(360, 170))
        AddLevelWindow.setMaximumSize(QtCore.QSize(360, 170))
        self.gridLayout = QtWidgets.QGridLayout(AddLevelWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.name_layout = QtWidgets.QHBoxLayout()
        self.name_layout.setObjectName("name_layout")
        self.name_label = QtWidgets.QLabel(AddLevelWindow)
        self.name_label.setObjectName("name_label")
        self.name_layout.addWidget(self.name_label)
        self.line_name = QtWidgets.QLineEdit(AddLevelWindow)
        self.line_name.setObjectName("line_name")
        self.name_layout.addWidget(self.line_name)
        self.main_layout.addLayout(self.name_layout)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddLevelWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.main_layout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.main_layout, 0, 0, 1, 1)

        self.retranslateUi(AddLevelWindow)
        self.buttonBox.accepted.connect(AddLevelWindow.accept)
        self.buttonBox.rejected.connect(AddLevelWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(AddLevelWindow)

    def retranslateUi(self, AddLevelWindow):
        _translate = QtCore.QCoreApplication.translate
        AddLevelWindow.setWindowTitle(_translate("AddLevelWindow", "Уровни"))
        self.name_label.setText(_translate("AddLevelWindow", "Название уровня"))

    def convert(self):
        return {"level_name": self.line_name.text()}

    def accept(self):
        if add_window.add_level(self.convert()):
            return super().accept()
        QtWidgets.QMessageBox.about(self, "Ошибка", "Ошибка")

