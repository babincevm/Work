# -*- coding: utf-8 -*-
from views import add_window
from PyQt5 import QtCore, QtGui, QtWidgets


class addCenter(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(addCenter, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(371, 304)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
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
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.line_headname = QtWidgets.QLineEdit(Dialog)
        self.line_headname.setObjectName("line_headname")
        self.horizontalLayout_2.addWidget(self.line_headname)
        self.incorrect_headname = QtWidgets.QLabel(Dialog)
        self.incorrect_headname.setObjectName("incorrect_headname")
        self.incorrect_headname.setVisible(False)
        self.horizontalLayout_2.addWidget(self.incorrect_headname)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.line_phone = QtWidgets.QLineEdit(Dialog)
        self.line_phone.setObjectName("line_phone")
        self.horizontalLayout_3.addWidget(self.line_phone)
        self.incorrect_phone = QtWidgets.QLabel(Dialog)
        self.incorrect_phone.setObjectName("incorrect_phone")
        self.incorrect_phone.setVisible(False)
        self.horizontalLayout_3.addWidget(self.incorrect_phone)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.line_adres = QtWidgets.QLineEdit(Dialog)
        self.line_adres.setObjectName("line_adres")
        self.horizontalLayout_4.addWidget(self.line_adres)
        self.incorrect_adres = QtWidgets.QLabel(Dialog)
        self.incorrect_adres.setObjectName("incorrect_adres")
        self.incorrect_adres.setVisible(False)
        self.horizontalLayout_4.addWidget(self.incorrect_adres)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
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
        self.label.setText(_translate("Dialog", "Название центра"))
        self.incorrect_name.setText(_translate("Dialog", "Введено неверно"))
        self.label_3.setText(_translate("Dialog", "Имя директора"))
        self.incorrect_headname.setText(_translate("Dialog", "Введено неверно"))
        self.label_5.setText(_translate("Dialog", "Номер телефона"))
        self.line_phone.setInputMask(_translate("Dialog", "0-000-000-0000"))
        self.incorrect_phone.setText(_translate("Dialog", "Введено неверно"))
        self.label_7.setText(_translate("Dialog", "Адрес"))
        self.incorrect_adres.setText(_translate("Dialog", "Введено неверно"))

    def check_data(self):
        flag = True

        self.incorrect_name.setVisible(False)
        self.incorrect_phone.setVisible(False)
        self.incorrect_headname.setVisible(False)
        self.incorrect_adres.setVisible(False)

        if not len(self.line_name.text()) > 10:
            self.incorrect_name.setVisible(True)
            flag = False

        if not len(self.line_phone.text()) == 14:
            flag = False
            self.incorrect_phone.setVisible(True)

        if not len(self.line_headname.text()) > 10:
            self.incorrect_headname.setVisible(True)
            flag = False

        if not len(self.line_adres.text()) > 10:
            self.incorrect_adres.setVisible(True)
            flag = False

        return flag

    def convert(self):
        return {"center_name": self.line_name.text(),
                "center_phone": self.line_phone.text(),
                "center_head_name": self.line_headname.text(),
                "center_address": self.line_adres.text()}

    def accept(self):
        if self.check_data():
            if add_window.add_center(self.convert()):
                return super().accept()
            QtWidgets.QMessageBox.about(self, "Ошибка", "Ошибка")
