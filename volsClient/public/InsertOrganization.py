# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from views import add_window


class AddOrgWindow(QtWidgets.QDialog):
    def __init__(self, parent):
        super(AddOrgWindow, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(472, 248)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(70, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line_name = QtWidgets.QLineEdit(Dialog)
        self.line_name.setObjectName("line_name")
        self.horizontalLayout.addWidget(self.line_name)
        self.incorrect_name = QtWidgets.QLabel(Dialog)
        self.incorrect_name.setObjectName("incorrect_name")
        self.incorrect_name.setVisible(False)
        self.horizontalLayout.addWidget(self.incorrect_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(70, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.line_email = QtWidgets.QLineEdit(Dialog)
        self.line_email.setObjectName("line_email")
        self.horizontalLayout_2.addWidget(self.line_email)
        self.incorrect_email = QtWidgets.QLabel(Dialog)
        self.incorrect_email.setObjectName("incorrect_email")
        self.incorrect_email.setVisible(False)
        self.horizontalLayout_2.addWidget(self.incorrect_email)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btn_submit = QtWidgets.QDialogButtonBox(Dialog)
        self.btn_submit.setOrientation(QtCore.Qt.Horizontal)
        self.btn_submit.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.btn_submit.setObjectName("btn_submit")
        self.verticalLayout.addWidget(self.btn_submit)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.btn_submit.accepted.connect(self.accept)
        self.btn_submit.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Название"))
        self.incorrect_name.setText(_translate("Dialog", "Введено неверно"))
        self.label_2.setText(_translate("Dialog", "Email"))
        self.incorrect_email.setText(_translate("Dialog", "Введено неверно"))

    def check_data(self):
        flag = True
        self.incorrect_email.setVisible(False)
        self.incorrect_name.setVisible(False)

        if not len(self.line_name.text()) > 10:
            self.incorrect_name.setVisible(True)
            flag = False

        if "@" not in self.line_email.text():
            flag = False
            self.incorrect_email.setVisible(True)
        return flag

    def convert(self):
        return {"org_name": self.line_name.text(),
                "org_email": self.line_email.text()}

    def accept(self):
        if self.check_data():
            if add_window.add_org(self.convert()):
                return super().accept()
            QtWidgets.QMessageBox.about(self, "Ошибка", "Ошибка")
